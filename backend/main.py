import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from youtube_downloader import download_youtube_video
from transcription import transcribe_audio
from blog_scraper import scrape_blog
from seo_optimizer import generate_seo_keywords
from article_generator import generate_article

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update this with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UrlInput(BaseModel):
    url: str

@app.post("/process")
async def process_url(input: UrlInput):
    try:
        if "youtube.com" in input.url or "youtu.be" in input.url:
            logger.info(f"Downloading YouTube video: {input.url}")
            video_path = download_youtube_video(input.url)
            logger.info(f"Video downloaded: {video_path}")
            
            logger.info(f"Transcribing audio from file: {video_path}")
            transcription = transcribe_audio(video_path)
            logger.info("Audio transcribed successfully")
        else:
            logger.info(f"Scraping blog: {input.url}")
            blog_content = scrape_blog(input.url)
            transcription = blog_content
            logger.info("Blog scraped")

        logger.info("Generating SEO keywords")
        keywords = generate_seo_keywords(transcription)
        logger.info("SEO keywords generated")

        logger.info("Generating article")
        article = generate_article(transcription, keywords)
        logger.info("Article generated")

        return {
            "transcription": transcription,
            "article": article,
            "keywords": keywords
        }
    except Exception as e:
        logger.error(f"Error processing URL: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))