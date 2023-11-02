import sys
import re
import requests

def enum_users(site_url):
    feed_url = f"{site_url}/?feed=rss2"
    author_url = f"{site_url}/?author="

    response = requests.get(feed_url)
    wp_users_feed = re.findall(r"<dc:creator>[<!\[CDATA\[]*(.+?)[\]\]>]*</dc:creator>", response.text)

    wp_users_author = []
    for user_id in range(1, 50):
        author_response = requests.get(f"{author_url}{user_id}")
        wp_user = re.findall(r"author author-(.+?) ", author_response.text, re.IGNORECASE)
        if wp_user:
            wp_users_author.extend(wp_user)

    wp_users = list(set(wp_users_feed + wp_users_author))
    if wp_users:
        for user in wp_users:
            print(user)
    else:
        print("No WordPress usernames found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <site_url>")
    else:
        site_url = sys.argv[1]
        enum_users(site_url)
