# Movie Recommendation System

A compact Streamlit app that finds a movie from an approximate title and suggests five other movies sharing at least one genre. It uses the bundled MovieLens 100K movie metadata and runs without an API key.

**Status:** educational demo. Recommendations use genre overlap rather than a trained collaborative-filtering model or personal viewing history.

## Quick start

Use Python 3.10+ with pip.

```sh
git clone https://github.com/mukheshvadlamudi/Movie-Recommendation-System.git
cd Movie-Recommendation-System
python -m venv .venv
```

Activate with `.venv\Scripts\Activate.ps1` in PowerShell or `source .venv/bin/activate` on macOS/Linux:

```sh
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local address printed by Streamlit, usually [http://localhost:8501](http://localhost:8501). Enter a title such as `Toy Story` and select **Get Recommendations**. Run the command from the repository root so the relative dataset path resolves.

## How recommendations work

1. Load `ml-100k/u.item` with pandas and normalize movie titles to lowercase.
2. Use `thefuzz` to find the closest title. The match is accepted only when its score is greater than 80.
3. Select other movies sharing at least one genre with the matched movie.
4. Sample five candidates with `random_state=42` and display their titles.

Results are reproducible for the same dataset and input. The app does not rank candidates by similarity, popularity, ratings, or release date. It reads movie metadata rather than the bundled user ratings.

## Project layout

| Path | Purpose |
| --- | --- |
| `app.py` | Dataset loading, fuzzy matching, genre filtering, and Streamlit UI |
| `requirements.txt` | Streamlit, pandas, and thefuzz dependencies |
| `ml-100k/` | Bundled MovieLens 100K data and its documentation |

## Data and limitations

MovieLens 100K contains older movie titles. The repository includes the data, so no separate download is needed for a normal clone. Review the original dataset terms in [ml-100k/README](ml-100k/README) before redistributing or using it beyond this demo.

The app needs readable metadata at `ml-100k/u.item`. Image posters, account support, and personalized recommendations are not implemented. Sampling assumes at least five matching candidates; a smaller replacement dataset may need additional handling. After dependencies are installed, recommendation generation does not call an external model service.

## Development and contributing

No automated test suite is included. To check a change, try a known title, a minor typo, and a title absent from the dataset. Confirm the matched movie is excluded from its five suggestions. Include these results with a focused pull request.

Useful extensions include ranking by genre similarity, handling small candidate sets, and tests for title matching. Keep dataset attribution and its separate terms intact.

## License

No license for the application code is included. Dataset terms are separate from code licensing; the owner needs to choose a code license before an open-source release.
