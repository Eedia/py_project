import os

# 현재 스크립트 기준 디렉터리 경로
current_dir = os.path.dirname(os.path.abspath(__file__))
monitor_dir = os.path.join(current_dir, "monitor_directory")

# 감시 회피용 '정상 파일' 정의
normal_files = {
    "info.txt": """이 파일은 일반 정보 파일입니다.
개인정보나 SQL 문은 포함되어 있지 않습니다.""",

    "logfile.log": """[INFO] 2025-06-15 12:00:00 - 서비스가 정상 작동 중입니다.""",

    "report.csv": """id,name,result
1,홍길동,pass
2,이몽룡,fail""",

    "summary.md": """# 보고서 요약
이 마크다운 문서는 감시에 걸리지 않습니다.
- 확장자: .md
- 내용: 정상적 텍스트
"""
}


def create_safe_files():
    """정상 파일 생성"""
    os.makedirs(monitor_dir, exist_ok=True)

    for filename, content in normal_files.items():
        file_path = os.path.join(monitor_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"정상 파일 생성 완료: {filename}")
    print("\nmonitor_directory 에 정상 파일이 생성되었습니다.")


def delete_safe_files():
    """정상 파일 삭제"""
    if not os.path.exists(monitor_dir):
        print("monitor_directory 가 존재하지 않습니다.")
        return

    deleted = False
    for filename in normal_files:
        file_path = os.path.join(monitor_dir, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"삭제 완료: {filename}")
            deleted = True

    if not deleted:
        print("삭제할 정상 파일이 존재하지 않습니다.")
    else:
        print("모든 정상 파일 삭제 완료.")


def main():
    """메뉴 기반 실행"""
    while True:
        print("\n정상 파일 관리 메뉴")
        print("1. 정상 파일 생성")
        print("2. 정상 파일 삭제")
        print("0. 종료")

        choice = input("선택 (1/2/0): ").strip()

        if choice == "1":
            create_safe_files()
        elif choice == "2":
            delete_safe_files()
        elif choice == "0":
            print("종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1, 2 또는 0을 입력하세요.")


if __name__ == "__main__":
    main()
