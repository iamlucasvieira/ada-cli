"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Ada CLI."""


if __name__ == "__main__":
    main(prog_name="ada-cli")  # pragma: no cover
