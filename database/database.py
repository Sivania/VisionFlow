import sqlite3
import json
#Connect
def connect():
    conn = sqlite3.connect('actions.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Actions (
            action_id INTEGER PRIMARY KEY AUTOINCREMENT,
            action_type TEXT NOT NULL,
            parameters TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ActionCompositions (
            composition_id INTEGER PRIMARY KEY AUTOINCREMENT,
            parent_action_id INTEGER NOT NULL,
            subaction_id INTEGER NOT NULL,
            order INTEGER NOT NULL,
            FOREIGN KEY (parent_action_id) REFERENCES Actions (action_id),
            FOREIGN KEY (subaction_id) REFERENCES Actions (action_id)
        );
    ''')

    conn.commit()
    cursor.close()

    return conn

def saveAction(conn, actionJson):
    # Assuming actionJson is a dictionary like {'name': 'Action Name', 'type': 'Action Type', 'parameters': {...}}

    # Convert parameters dict to JSON string
    params_json = json.dumps(actionJson['parameters'])

    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Actions (action_type, parameters) VALUES (?, ?)
    ''', (actionJson['type'], params_json))
    
    # Commit the changes and close the cursor
    conn.commit()
    cursor.close()

    return cursor.lastrowid  # Returns the id of the last inserted row

