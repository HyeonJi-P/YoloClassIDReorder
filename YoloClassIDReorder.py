import argparse
import os

def class_order_match(before_txt_path, after_txt_path):
    # class name list
    before_list = []
    after_list = []
    # Class_re_order 리스트
    class_re_order = []

    # 이전 파일 읽기
    with open(before_txt_path, "r") as f:
        for line in f:
            # 한 줄의 단어를 리스트에 추가
            before_list.append(line.strip())

    # 수정 파일 읽기
    with open(after_txt_path, "r") as f:
        for line in f:
            # 한 줄의 단어를 리스트에 추가
            after_list.append(line.strip())

    # 이전 파일 단어 순서대로 반복
    for word in before_list:
        # 수정 파일에서 단어 위치 찾기
        index = after_list.index(word)

        # Class_re_order 리스트에 위치 추가
        class_re_order.append(index)
    
    print("Before_classID_order:",before_list)
    print("after_classID_order:",after_list)

    print("[Class name]: Old Index => New Index")
    for idx in range(len(class_re_order)):
        print("["+before_list[idx]+"]: "+str(idx)+" => "+str(class_re_order[idx]))

    return class_re_order


def YoloClassIDReorder(folder_path, before_txt_path, after_txt_path):
    # 폴더 내 모든 txt 파일 목록 가져오기
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt") and not f.endswith("classes.txt")]
    #print(txt_files)

    # 클래스 번호 리스트
    class_numbers = class_order_match(before_txt_path, after_txt_path)
    
    # 폴더 내 txt 파일 하나씩 반복
    for file in txt_files:

        # txt 파일 열기
        with open(os.path.join(folder_path, file), "r") as f:
            
            new_lines=[]
            for line in f: # 파일 내용을 한 줄씩 읽기
                
                # 숫자 5개를 리스트로 저장
                numbers = list(map(float, line.split()))
                # 첫 번째 숫자(class 번호) 저장
                class_number = int(numbers[0])
                #print("원본:",class_number)

                # 리스트에서 class 번호와 일치하는 인덱스 찾기
                index = class_numbers.index(class_number)

                # 수정된 class 번호(인덱스) 리스트에 추가
                numbers[0] = index

                # 수정된 내용 문자열로 변환
                new_line = " ".join(map(str, numbers))
                new_lines.append(new_line)

            #print("수정결과:",new_lines)
            # 파일 내용 수정
            with open(os.path.join(folder_path, file), "w") as txtF:
                for new_line in new_lines:
                    #print(new_line)
                    txtF.write(new_line+"\n")



# 옵션 정의
parser = argparse.ArgumentParser()
parser.add_argument("--txt_data", type=str, required=True, help="폴더 경로")
parser.add_argument("--before_txt_path", type=str, required=True, help="변경 전 주석 파일")
parser.add_argument("--after_txt_path", type=str, default="reordered.txt", help="변경 후 주석 파일")
parser.add_argument("--class_mapping", type=str, nargs="*", default=[], help="클래스 ID 매핑")

# 옵션 분석
args = parser.parse_args()

# 폴더 경로 유효성 검사
if not os.path.isdir(args.txt_data):
    print("폴더 경로가 유효하지 않습니다.")
    exit()

# 주석 파일 유효성 검사
if not os.path.isfile(args.before_txt_path):
    print("변경 전 주석 파일 경로가 유효하지 않습니다.")
    exit()
if not os.path.isfile(args.after_txt_path):
    print("변경 전 주석 파일 경로가 유효하지 않습니다.")
    exit()


YoloClassIDReorder(args.txt_data, args.before_txt_path, args.after_txt_path)

# 폴더 경로
folder_path = "D:\ALARAD_2024_images\YOLO_ClassEditing"
# path
before_txt_path = "./YOLO_ClassEditing/labelme_classes.txt"
after_txt_path = "./YOLO_ClassEditing/yolo_classes.txt"
