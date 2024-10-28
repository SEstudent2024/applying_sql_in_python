import sqlite3

def add_member(id, name, age):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO Members (id, name, age) VALUES (?, ?, ?)
        ''', (id, name, age))
        
        conn.commit()
        print("Member added successfully.")

    except sqlite3.IntegrityError as e:
        print(f"Error: {e}. The member ID already exists or another constraint is violated.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()

add_member(1, 'John Doe', 25)

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT id FROM Members WHERE id = ?', (member_id,))
        if cursor.fetchone() is None:
            raise ValueError("Member ID does not exist.")
        
        cursor.execute('''
            INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) 
            VALUES (?, ?, ?, ?)
        ''', (member_id, date, duration_minutes, calories_burned))
        
        conn.commit()
        print("Workout session added successfully.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()

add_workout_session(1, '2023-08-11', 60, 500)

def update_member_age(member_id, new_age):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT id FROM Members WHERE id = ?', (member_id,))
        if cursor.fetchone() is None:
            raise ValueError("Member ID does not exist.")
        
        cursor.execute('''
            UPDATE Members SET age = ? WHERE id = ?
        ''', (new_age, member_id))
        
        conn.commit()
        print("Member age updated successfully.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()

update_member_age(1, 26)

def delete_workout_session(session_id):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT session_id FROM WorkoutSessions WHERE session_id = ?', (session_id,))
        if cursor.fetchone() is None:
            raise ValueError("Session ID does not exist.")
        
        cursor.execute('''
            DELETE FROM WorkoutSessions WHERE session_id = ?
        ''', (session_id,))
        
        conn.commit()
        print("Workout session deleted successfully.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()

delete_workout_session(1)

def get_members_in_age_range(start_age, end_age):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM Members WHERE age BETWEEN ? AND ?
        ''', (start_age, end_age))
        
        members = cursor.fetchall()
        for member in members:
            print(member)
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()

get_members_in_age_range(25, 30)