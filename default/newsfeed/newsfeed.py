from default.pod import PodInterface
from dash import html

import feedparser


class NewsFeed(PodInterface):
    def __init__(self, config):
        self.config = config
        self.feeds = []
        for item in self.config["feeds"]:
            feed = NewsFeed.get_feed(item["url"])
            self.feeds.append(feed)
            feed = None

    def content(self):
        list_items = []
        for feed in self.feeds:
            for item in feed.entries:
                css_class = ""
                if len(list_items) == 0:
                    css_class = "active"
                list_item = html.Li(children=[], className=css_class)
                if self.config["show_source_title"] or self.config["config.show_source_date"]:
                    title_date = html.Div(children=[], className="newsfeed-source light small dimmed")
                    feed_title = ""
                    if self.config["show_source_title"]:
                        feed_title = feed.feed.title
                    if self.config["show_source_date"] and hasattr(feed.feed, "published"):
                        if self.config["show_source_title"] and len(feed_title) > 0:
                            feed_title += " - "
                            feed_title += feed.feed.published
                    title_date.children.append(feed_title)
                    list_item.children.append(title_date)
                list_item.children.append(html.Div(children=item.title, className="newsfeed-title bright medium light no-wrap"))
                list_items.append(list_item)
        return html.Ul(children=list_items, className="newsfeed-list")


    @classmethod
    def get_feed(cls, url):
        # @todo Add exception handling
        f = feedparser.parse(url)
        return f


