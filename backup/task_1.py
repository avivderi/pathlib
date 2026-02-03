from pathlib import Path

# שאלה 1: יצירת נתיבים
print("--- Question 1 ---")
print("תיקיה נוכחית:", Path.cwd())

path1 = Path("files") / "data.txt" # ככה מחברים נתיבים
print("הנתיב לקובץ:", path1)
print("נתיב מלא לתיקיה:", path1.absolute().parent)
print("תיקיית הבית:", Path.home())

# שאלה 2: בדיקת קיום
print("\n--- Question 2 ---")
my_file = Path("notes.txt")
if my_file.exists():
    print("הקובץ קיים")
else:
    my_file.write_text('זהו קובץ חדש שנוצר ע"י pathlib')
    print("יצרתי קובץ חדש!")
print("התוכן שלו:", my_file.read_text())

# שאלה 3: מידע על קובץ
print("\n--- Question 3 ---")
p = Path('documents/reports/annual_report.pdf')
print("שם הקובץ:", p.name)
print("בלי סיומת:", p.stem)
print("רק סיומת:", p.suffix)
print("אבא שלו:", p.parent)
print("כל האבות:", list(p.parents))
# תשובה: הקובץ לא חייב להיות קיים בשביל זה!

# שאלה 4: רשימת קבצים
print("\n--- Question 4 ---")
f_count = 0
d_count = 0
for item in Path.cwd().iterdir():
    if item.is_dir():
        print("[תיקייה]", item.name)
        d_count = d_count + 1
    else:
        print("[קובץ]", item.name)
        f_count = f_count + 1
print("סה''כ קבצים:", f_count, "סה''כ תיקיות:", d_count)

# שאלה 5: חיפוש לפי סיומת
print("\n--- Question 5 ---")
pys = list(Path.cwd().glob("*.py"))
txts = list(Path.cwd().glob("*.txt"))
print("כמה py:", len(pys))
print("כמה txt:", len(txts))

# שאלה 6: יצירת פרויקט
print("\n--- Question 6 ---")
project = Path("my_project")
(project / "src").mkdir(parents=True, exist_ok=True)
(project / "tests").mkdir(parents=True, exist_ok=True)
(project / "docs").mkdir(parents=True, exist_ok=True)
(project / "data").mkdir(parents=True, exist_ok=True)
(project / "README.md").write_text("hello")

# שאלה 7: גיבוי
print("\n--- Question 7 ---")
Path("backup").mkdir(exist_ok=True)
for f in Path.cwd().glob("*.py"):
    content = f.read_bytes()
    (Path("backup") / f.name).write_bytes(content)
    print("העתקתי את:", f.name)

# שאלה 8: גודל קבצים
print("\n--- Question 8 ---")
total = 0
big_file = ""
big_size = 0
for f in Path.cwd().iterdir():
    if f.is_file():
        s = f.stat().st_size
        print(f.name, "גודל:", s)
        total = total + s
        if s > big_size:
            big_size = s
            big_file = f.name
print("סה''כ גודל:", total)
print("הכי גדול:", big_file)

# שאלה 9: מילון סיומות
print("\n--- Question 9 ---")
my_dict = {}
for f in Path.cwd().iterdir():
    if f.is_file():
        ext = f.suffix
        if ext in my_dict:
            my_dict[ext] = my_dict[ext] + 1
        else:
            my_dict[ext] = 1
print("מילון סיומות:", my_dict)

# שאלה 10: מנהל קבצים
print("\n--- Question 10 ---")
while True:
    print("1.הצג 2.חפש 3.תיקיה 4.מחק 5.שם 6.צא")
    cmd = input("מה לעשות? ")
    if cmd == "1":
        for item in Path.cwd().iterdir(): print(item.name)
    elif cmd == "2":
        suf = input("איזה סיומת? ")
        for f in Path.cwd().glob("*" + suf): print(f.name)
    elif cmd == "3":
        name = input("שם תיקיה? ")
        Path(name).mkdir(exist_ok=True)
    elif cmd == "4":
        name = input("איזה קובץ למחוק? ")
        Path(name).unlink()
    elif cmd == "5":
        old = input("שם ישן? ")
        new = input("שם חדש? ")
        Path(old).rename(new)
    elif cmd == "6":
        break
