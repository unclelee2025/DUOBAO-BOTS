import sqlite3
import time
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "data" / "group.db"

class GroupDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self._init()

    def _init(self):
        cur = self.conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS group_members (
            chat_id INTEGER,
            user_id INTEGER,
            join_time INTEGER,
            PRIMARY KEY (chat_id, user_id)
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS violations (
            chat_id INTEGER,
            user_id INTEGER,
            count INTEGER,
            last_time INTEGER,
            PRIMARY KEY (chat_id, user_id)
        )
        """)

        self.conn.commit()

    def record_join(self, chat_id, user_id):
        self.conn.execute(
            "REPLACE INTO group_members VALUES (?, ?, ?)",
            (chat_id, user_id, int(time.time()))
        )
        self.conn.commit()

    def get_join_time(self, chat_id, user_id):
        row = self.conn.execute(
            "SELECT join_time FROM group_members WHERE chat_id=? AND user_id=?",
            (chat_id, user_id)
        ).fetchone()
        return row[0] if row else None

    def add_violation(self, chat_id, user_id):
        row = self.conn.execute(
            "SELECT count FROM violations WHERE chat_id=? AND user_id=?",
            (chat_id, user_id)
        ).fetchone()

        count = (row[0] + 1) if row else 1

        self.conn.execute(
            "REPLACE INTO violations VALUES (?, ?, ?, ?)",
            (chat_id, user_id, count, int(time.time()))
        )
        self.conn.commit()
        return count


class PointsDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._init()

    def _init(self):
        cur = self.conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS points_users (
                chat_id INTEGER,
                user_id INTEGER,
                points INTEGER DEFAULT 0,
                last_sign_date TEXT,
                sign_streak INTEGER DEFAULT 0,
                PRIMARY KEY (chat_id, user_id)
            )
            """
        )
        self.conn.commit()

    def _today(self) -> datetime.date:
        return datetime.date.fromtimestamp(time.time())

    def _ensure_user(self, chat_id, user_id):
        row = self.conn.execute(
            """
            SELECT points, last_sign_date, sign_streak
            FROM points_users
            WHERE chat_id=? AND user_id=?
            """,
            (chat_id, user_id),
        ).fetchone()

        if not row:
            self.conn.execute(
                """
                INSERT INTO points_users (chat_id, user_id, points, last_sign_date, sign_streak)
                VALUES (?, ?, 0, NULL, 0)
                """,
                (chat_id, user_id),
            )
            self.conn.commit()
            row = self.conn.execute(
                """
                SELECT points, last_sign_date, sign_streak
                FROM points_users
                WHERE chat_id=? AND user_id=?
                """,
                (chat_id, user_id),
            ).fetchone()

        return row

    def sign(self, chat_id, user_id, reward=2):
        today = self._today()
        row = self._ensure_user(chat_id, user_id)

        points = row["points"] or 0
        last_date_raw = row["last_sign_date"]
        streak = row["sign_streak"] or 0

        if last_date_raw:
            try:
                last_date = datetime.date.fromisoformat(last_date_raw)
            except ValueError:
                last_date = None
        else:
            last_date = None

        if last_date == today:
            # Already signed today
            return False, streak, points, 0

        if last_date and (today - last_date).days == 1:
            streak += 1
        else:
            streak = 1

        bonus = 2 if (streak % 7 == 0) else 0
        points += reward + bonus

        self.conn.execute(
            """
            UPDATE points_users
            SET points=?, last_sign_date=?, sign_streak=?
            WHERE chat_id=? AND user_id=?
            """,
            (points, today.isoformat(), streak, chat_id, user_id),
        )
        self.conn.commit()

        return True, streak, points, bonus

    def get_state(self, chat_id, user_id):
        row = self._ensure_user(chat_id, user_id)
        return {
            "points": row["points"] or 0,
            "last_sign_date": row["last_sign_date"],
            "sign_streak": row["sign_streak"] or 0,
        }

    def last_draws(self, limit=5):
        """
        Placeholder: return recent draws.
        TODO: replace with real query when draw data is stored.
        """
        return []
