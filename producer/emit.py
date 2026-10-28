"""Week 1: send fake page views to the `events` topic.

Run (after Redpanda is up):
    python -m producer.emit --rate 5 --users 10
"""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rate", type=int, default=1, help="events per second")
    parser.add_argument("--users", type=int, default=5)
    args = parser.parse_args()
    print(f"TODO week 1: publish {args.rate}/s for {args.users} users to topic events")


if __name__ == "__main__":
    main()
