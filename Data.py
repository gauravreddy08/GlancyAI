import pandas as pd

class Data():
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.data = self.data[['id', 'title', 'channel', 'views', 'publish_time', 'url_suffix']]
        self._preprocess()

    def _preprocess(self):
        self.data['views'] = self.data['views'].apply(self.__convert_views)
        self.data['publish_time'] = self.data['publish_time'].apply(self.__convert_publish_time)
        self.__remove_shorts()
    def __convert_views(self, views_str):
        if 'No' in views_str: return 0
        return int(views_str.replace(' views', '').replace(',', ''))
    
    def __convert_publish_time(self, publish_time):
        publish_time.replace('Streamed ', '')
        if 'months ago' in publish_time:
            months = int(publish_time.replace(' months ago', '').strip())
            return pd.Timestamp.now() - pd.DateOffset(months=months)
        elif 'years ago' in publish_time:
            years = int(publish_time.replace(' years ago', '').strip())
            return pd.Timestamp.now() - pd.DateOffset(years=years)
        else:
            return pd.Timestamp.now()  # For any other cases
    
    def __remove_shorts(self):
        self.data = self.data[~self.data['url_suffix'].str.startswith('/shorts')]
    
    def filter(self, count=10, min_latest=5):
        count = min(count, len(self.data))
        min_latest = min(min_latest, len(self.data))

        one_year_ago = pd.Timestamp.now() - pd.DateOffset(years=1)
        videos_one_year_ago = self.data[self.data['publish_time'] <= one_year_ago]

        videos_one_year_ago = videos_one_year_ago.sort_values(by='views', ascending=False)

        top_videos_one_year_ago = videos_one_year_ago.head(min_latest)

        remaining_videos = self.data[~self.data['id'].isin(top_videos_one_year_ago['id'])].sort_values(by='views', ascending=False)
        self.data = pd.concat([top_videos_one_year_ago, remaining_videos.head(count - len(top_videos_one_year_ago))])