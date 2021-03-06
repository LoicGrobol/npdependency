import pathlib

from typing import Iterable, List, TextIO

import click
import click_pathlib

from npdependency import conll2018_eval as evaluator


CONLL_METRICS = [
    "Tokens",
    "Sentences",
    "Words",
    "UPOS",
    "XPOS",
    "UFeats",
    "AllTags",
    "Lemmas",
    "UAS",
    "LAS",
    "CLAS",
    "MLAS",
    "BLEX",
]


@click.command()
@click.argument(
    "gold_file",
    type=click_pathlib.Path(resolve_path=True, exists=True, dir_okay=False),
)
@click.argument(
    "syst_files",
    type=click_pathlib.Path(resolve_path=True, exists=True, dir_okay=False),
    nargs=-1,
)
@click.option(
    "--out_file",
    type=click.File("w"),
    default="-",
)
def make_csv_summary(
    syst_files: Iterable[pathlib.Path],
    gold_file: pathlib.Path,
    out_file: TextIO,
):
    gold_conllu = evaluator.load_conllu_file(gold_file)

    header = ["name", *(f"{m}_{p}" for p in ("P", "R", "F") for m in CONLL_METRICS)]
    print(",".join(header), file=out_file)
    for syst_file in syst_files:
        syst_conllu = evaluator.load_conllu_file(syst_file)
        metrics = evaluator.evaluate(gold_conllu, syst_conllu)
        row: List[str] = [syst_file.stem]
        for m in CONLL_METRICS:
            mres = metrics[m]
            row.extend((str(mres.precision), str(mres.recall), str(mres.f1)))
        print(",".join(row), file=out_file)


if __name__ == "__main__":
    make_csv_summary()
