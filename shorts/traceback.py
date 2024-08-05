import click
import sys

sys.tracebacklimit = 1

@click.command()
@click.option('--num', prompt='Enter a numerator', help='Enter a numerator')
@click.option('--deno', prompt='Enter a denominator',
              help='Enter a denominator')
def divide(num, deno):
    """Simple program that divides two numbers."""
    quo = float(num)/float(deno)
    click.echo(f"Quotient = {quo}")

if __name__ == '__main__':
    divide()