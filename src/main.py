from arxiv import fetch
from deepl import translate
from model.paper import Paper
from utils.log import logger


def main():
    """
    Fetch papers from arxiv.org
    """
    entries = fetch()
    papers = [Paper(entry=e) for e in entries]
    todays_entry = [paper for paper in papers if paper.is_todays_entry]
    for entry in todays_entry:
        translated = translate(entry)
        logger.debug(translated)


if __name__ == "__main__":
    main()
