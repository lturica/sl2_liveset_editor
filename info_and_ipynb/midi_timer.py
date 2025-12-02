#!/usr/bin/env python3
import argparse
import sys
import time
import mido


def choose_output(port_hint: str | None) -> mido.ports.BaseOutput:
    outs = mido.get_output_names()
    if not outs:
        print(
            "No MIDI outputs found. Is your interface connected and recognized by the OS?",
            file=sys.stderr,
        )
        sys.exit(1)

    if port_hint:
        for name in outs:
            if port_hint.lower() in name.lower():
                print(f"Opening MIDI out: {name}")
                return mido.open_output(name)
        # If we didn't find a match, show options and exit
        print(
            f"Couldn't find an output containing '{port_hint}'. Available outputs:",
            file=sys.stderr,
        )
        for name in outs:
            print(f"  - {name}", file=sys.stderr)
        sys.exit(1)
    else:
        # If no hint given and only one port exists, use it; otherwise show choices.
        if len(outs) == 1:
            print(f"Opening only available MIDI out: {outs[0]}")
            return mido.open_output(outs[0])
        else:
            print(
                "Multiple MIDI outputs available. Use --port to pick one. Available outputs:",
                file=sys.stderr,
            )
            for name in outs:
                print(f"  - {name}", file=sys.stderr)
            sys.exit(1)


def run_clock(out: mido.ports.BaseOutput, bpm: float):
    """
    Sends MIDI Clock (0xF8) at the specified BPM.
    Also sends Start (0xFA) on begin and Stop (0xFC) on Ctrl+C.
    MIDI Clock = 24 pulses per quarter note (PPQN).
    """
    ppqn = 24
    interval = 60.0 / (bpm * ppqn)
    print(
        f"Running MIDI Clock at {bpm:.2f} BPM (interval ~ {interval * 1000:.3f} ms between ticks)."
    )
    # Start
    out.send(mido.Message("start"))
    print("Sent MIDI Start. Press Ctrl+C to stop.")

    next_time = time.perf_counter()
    try:
        while True:
            # Send one clock tick
            out.send(mido.Message("clock"))
            # Schedule next tick
            next_time += interval
            # Sleep just enough; avoid negative sleep in case of drift
            sleep_for = next_time - time.perf_counter()
            if sleep_for > 0:
                time.sleep(sleep_for)
            else:
                # If we fall behind, catch up by nudging next_time
                next_time = time.perf_counter()
    except KeyboardInterrupt:
        pass
    finally:
        out.send(mido.Message("stop"))
        print("\nSent MIDI Stop. Goodbye!")


def run_countdown(
    out: mido.ports.BaseOutput,
    seconds: int,
    channel: int,
    note: int,
    cc: int,
    tick_ms: int,
):
    """
    Every second:
      - Send a short Note On/Off 'tick'
      - Send a Control Change with the remaining seconds (mod 128)
    At zero:
      - Send a small 'ding' (fifth interval)
    """
    channel = max(0, min(channel, 15))  # 0–15
    remaining = seconds
    print(
        f"Countdown: {seconds}s on MIDI channel {channel + 1}. Tick note={note}, CC={cc}. Press Ctrl+C to cancel."
    )

    t0 = time.perf_counter()
    next_sec = t0

    try:
        while remaining >= 0:
            now = time.perf_counter()
            if now >= next_sec:
                # Send CC with remaining seconds (wrap to 0–127)
                cc_val = remaining % 128
                out.send(
                    mido.Message(
                        "control_change", channel=channel, control=cc, value=cc_val
                    )
                )

                if remaining > 0:
                    # Tick note
                    out.send(
                        mido.Message("note_on", channel=channel, note=note, velocity=80)
                    )
                    time.sleep(tick_ms / 1000.0)
                    out.send(
                        mido.Message("note_off", channel=channel, note=note, velocity=0)
                    )
                    print(f"T-{remaining:>3}s (CC{cc}={cc_val})")
                else:
                    # Final ding: root + fifth briefly
                    out.send(
                        mido.Message(
                            "note_on", channel=channel, note=note, velocity=100
                        )
                    )
                    out.send(
                        mido.Message(
                            "note_on", channel=channel, note=note + 7, velocity=90
                        )
                    )
                    time.sleep(0.2)
                    out.send(
                        mido.Message("note_off", channel=channel, note=note, velocity=0)
                    )
                    out.send(
                        mido.Message(
                            "note_off", channel=channel, note=note + 7, velocity=0
                        )
                    )
                    print("Time's up!")
                    break

                remaining -= 1
                next_sec += 1.0
            else:
                time.sleep(min(0.01, (next_sec - now)))
    except KeyboardInterrupt:
        print("\nCancelled.")
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Send MIDI Clock or a MIDI-based countdown timer."
    )
    sub = parser.add_subparsers(dest="mode", required=True)

    p_clock = sub.add_parser("clock", help="Send MIDI Clock at a given BPM.")
    p_clock.add_argument(
        "--bpm", type=float, default=120.0, help="Beats per minute (default: 120.0)"
    )
    p_clock.add_argument(
        "--port", type=str, help="Substring of the MIDI output port name to open"
    )

    p_count = sub.add_parser(
        "countdown", help="Send a 1-second tick and CC with remaining seconds."
    )
    p_count.add_argument("seconds", type=int, help="How many seconds to count down")
    p_count.add_argument(
        "--port", type=str, help="Substring of the MIDI output port name to open"
    )
    p_count.add_argument(
        "--channel",
        type=int,
        default=0,
        help="MIDI channel 1–16 (enter 1–16; default: 1)",
    )
    p_count.add_argument(
        "--note", type=int, default=60, help="Tick note number (default: 60=C4)"
    )
    p_count.add_argument(
        "--cc",
        type=int,
        default=20,
        help="CC number to send remaining seconds on (default: 20)",
    )
    p_count.add_argument(
        "--tick-ms",
        type=int,
        default=60,
        help="Length of tick note in ms (default: 60)",
    )

    p_count = sub.add_parser("list", help="List available midi ports.")
    args = parser.parse_args()

    # Normalize channel to 0–15 if provided 1–16
    if args.mode == "countdown":
        if 1 <= args.channel <= 16:
            args.channel = args.channel - 1
        else:
            print("Channel must be 1–16.", file=sys.stderr)
            sys.exit(1)

    out = choose_output(getattr(args, "port", None))

    if args.mode == "clock":
        run_clock(out, args.bpm)
    elif args.mode == "countdown":
        run_countdown(out, args.seconds, args.channel, args.note, args.cc, args.tick_ms)
