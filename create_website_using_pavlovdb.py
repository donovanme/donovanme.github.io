import sqlite3
import json

def export_to_js(db_path, output_file):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Fetch all records from the questions table
        cursor.execute("SELECT id, question, answer FROM pavlovs where question is not null")
        records = cursor.fetchall()

        # Create a list of dictionaries from the records
        questions = [
            {
                "id": record[0],
                "q": record[1],
                "a": record[2],
            }
            for record in records
        ]

        # Write the list of dictionaries to a JS file
        with open(output_file, 'w') as f:
            f.write('const questions = ')
            json.dump(questions, f, indent=4)
            f.write(';')

        print(f"Data exported to {output_file} successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    db_path = 'c:\\data\\trivia_ai.db'  # Path to your SQLite database
    output_file = 'C:\code\donovanme.github.io\questions.js'  # Output JS file name
    export_to_js(db_path, output_file)
