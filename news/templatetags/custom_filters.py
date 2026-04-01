import re
from django import template
from django.utils.html import strip_tags

register = template.Library()


@register.filter
def strip_html_and_media(value, length=200):
    """
    Removes all HTML tags, iframes, and media elements from content
    Used for article previews in lists
    """
    if not value:
        return ""

    # Remove script and style tags
    value = re.sub(r'<script[^>]*>.*?</script>', '', value, flags=re.DOTALL | re.IGNORECASE)
    value = re.sub(r'<style[^>]*>.*?</style>', '', value, flags=re.DOTALL | re.IGNORECASE)

    # Remove iframe tags (for YouTube, etc.)
    value = re.sub(r'<iframe[^>]*>.*?</iframe>', '', value, flags=re.DOTALL | re.IGNORECASE)

    # Remove figure tags with media
    value = re.sub(r'<figure[^>]*>.*?</figure>', '', value, flags=re.DOTALL | re.IGNORECASE)

    # Strip remaining HTML tags
    text = strip_tags(value).strip()

    # Clean up multiple spaces
    text = re.sub(r'\s+', ' ', text)

    # Truncate to specified length
    if len(text) > length:
        text = text[:length].rsplit(' ', 1)[0] + '...'
    else:
        text = text + ('...' if len(strip_tags(value)) > length else '')

    return text


@register.filter
def youtube_embed(url):
    """
    Convert YouTube URL to embed iframe code
    Supports: youtube.com, youtu.be, youtube-nocookie.com
    """
    if not url:
        return ""

    # Extract video ID from various YouTube URL formats
    video_id = None

    # youtu.be/VIDEO_ID
    match = re.search(r'youtu\.be/([^?&\s]+)', url)
    if match:
        video_id = match.group(1)

    # youtube.com/watch?v=VIDEO_ID
    if not video_id:
        match = re.search(r'v=([^&\s]+)', url)
        if match:
            video_id = match.group(1)

    # youtube.com/embed/VIDEO_ID
    if not video_id:
        match = re.search(r'youtube\.com/embed/([^?&\s]+)', url)
        if match:
            video_id = match.group(1)

    if video_id:
        return f'<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/{video_id}" ' \
               f'title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; ' \
               f'encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" ' \
               f'allowfullscreen></iframe>'

    return ""
