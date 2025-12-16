class NBAApi {
	private endpoint = "http://api:8000/nba";

	async getGames() {
		try {
			const res = await fetch(this.endpoint + "/games");

			const data = await res.json();

			return data ?? [];
		} catch (error) {
			console.error("Failed to get NBA games: ", error);

			return [];
		}
	}
}

const nbaapi = new NBAApi();

export default nbaapi;
