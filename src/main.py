from arxiv import fetch
from utils.log import logger
from model.paper import Paper

def main():
    """
    Fetch papers from arxiv.org
    """
    entries = fetch()
    papers = [Paper(entry=e) for e in entries]
    todays_entry = [paper for paper in papers if paper.is_todays_entry]
    logger.debug(todays_entry[0].date)




if __name__ == "__main__":
    main()
