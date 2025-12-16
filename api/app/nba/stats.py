from nba_api.stats.endpoints import leaguegamefinder

def get_games(season="2023-24"):
    return leaguegamefinder.LeagueGameFinder(
        season_nullable=season
    ).get_dict()
