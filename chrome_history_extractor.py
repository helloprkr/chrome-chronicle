#!/usr/bin/env python3
import sqlite3
import os
from datetime import datetime, timedelta
import shutil

def extract_chrome_history():
    # Get today's date
    today = datetime.now()
    date_str = today.strftime('%Y-%m-%d')
    year_month = today.strftime('%Y-%m')
    
    # Path to Chrome's history database
    chrome_history_path = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/History')
    temp_history_path = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/History_temp')
    
    # Make sure base directory exists
    base_dir = os.path.dirname(os.path.realpath(__file__))
    month_dir = os.path.join(base_dir, f"{year_month}/")
    
    # Create month directory if it doesn't exist
    os.makedirs(month_dir, exist_ok=True)
    
    # Output file path
    output_file = os.path.join(month_dir, f"{date_str}_URL-History.md")
    
    # Copy the database file to avoid locking issues if Chrome is running
    try:
        shutil.copy2(chrome_history_path, temp_history_path)
    except Exception as e:
        print(f"Error copying Chrome history database: {e}")
        return
        
    try:
        # Connect to the copied database
        conn = sqlite3.connect(temp_history_path)
        cursor = conn.cursor()
        
        # Get today's timestamp range
        start_of_day = datetime.combine(today.date(), datetime.min.time())
        end_of_day = datetime.combine(today.date(), datetime.max.time())
        
        # Convert to Chrome time (microseconds since Jan 1, 1601)
        chrome_epoch = datetime(1601, 1, 1)
        start_time = int((start_of_day - chrome_epoch).total_seconds() * 1000000)
        end_time = int((end_of_day - chrome_epoch).total_seconds() * 1000000)
        
        # Query to fetch URLs visited today
        query = '''
        SELECT url, title, last_visit_time, visit_count
        FROM urls
        WHERE last_visit_time BETWEEN ? AND ?
        ORDER BY last_visit_time DESC
        '''
        cursor.execute(query, (start_time, end_time))
        
        # Prepare Markdown content
        md_content = f'# Browsing History for {date_str}\n\n'
        md_content += f'*Collected at: {datetime.now().strftime("%H:%M:%S")}*\n\n'
        md_content += '| Time | Title | URL | Visit Count |\n'
        md_content += '|------|-------|-----|------------|\n'
        
        # Fetch and format data
        results = cursor.fetchall()
        if not results:
            md_content += "*No browsing history recorded for today*\n"
        
        for row in results:
            url, title, last_visit, visit_count = row
            
            # Convert Chrome timestamp to datetime
            visit_time = chrome_epoch + timedelta(microseconds=last_visit)
            
            # Format for markdown table
            time_str = visit_time.strftime('%H:%M:%S')
            safe_title = title.replace('|', '\\|') if title else 'No Title'
            safe_url = url.replace('|', '%7C')
            
            md_content += f'| {time_str} | {safe_title} | {safe_url} | {visit_count} |\n'
        
        # Write to the Markdown file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(md_content)
            
        print(f"Chrome history saved to {output_file}")
        
    except Exception as e:
        print(f"Error extracting Chrome history: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
        
        # Remove temporary copy of history file
        try:
            os.remove(temp_history_path)
        except:
            pass

if __name__ == "__main__":
    extract_chrome_history() 