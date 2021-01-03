class Student:
    def __init__(self, name, std_no, grade_dict):
        self.name = name
        self.std_no = std_no
        self.grade_dict = grade_dict

    def getSum(self):
        total = 0
        for score in self.grade_dict.values():
            total += score
        return total

    def getAvg(self):
        return self.getSum() / len(self.grade_dict)

    def print_std(self):
        print("이름: ", self.name, "학번: ", self.std_no, end=" | ")
        for subject in self.grade_dict:
            print(subject,":",self.grade_dict[subject], end=" | ")
        print("총점:",self.getSum(), end=" | ")
        print("평균:", self.getAvg())


class SMS:
    def __init__(self):
        self.student_list = list()

    def insert(self, student):
        if self.find_idx(student.std_no) == -1:
            self.student_list.append(student)

        else:
            choice = input("이미 같은 학번의 학생이 존재합니다. 새로 입력한 학생의 정보로 기존 정보를 대체하겠습니까?")
            if choice == "Y" or choice == "y":
                self.student_list.pop(self.find_idx(student.std_no))
                self.student_list.append(student)
            elif choice == "N" or choice == 'n':
                print("정보가 그대로 유지됩니다.")
            else:
                print("올바른 값을 입력해주세요.")
        '''
        if len(self.student_list) == 0:
            self.student_list.append(student)

        else:
            for i in range(len(self.student_list)):   # if/else를 안두고 처음에 이 for문 만을 사용하여 코딩을 하려하면 초기에는 길이가 0이라서 작동이 되지 않음!!!!
                if self.student_list[i].std_no == student.std_no:
                    choice = input("이미 같은 학번의 학생이 존재합니다. 새로 입력한 학생의 정보로 기존 정보를 대체하겠습니까?")
                    if choice == "Y":
                        self.student_list.pop(self.student_list[i])
                        self.student_list.append(student)
                    elif choice == "N":
                        pass
                else:
                    self.student_list.append(student)
                    
            이렇게 코딩할 경우 else문에 대해 여러개가 출력됨. 왜냐하면 for문에서 index를 지정해 준 것이 아니라 그 범위에 대해 돌리는 것이기에 
            if가 아닐때 else가 실행되고 또 다시 else가 실행되어 self.student_list의 len만큼 반복되어 저장되게 된다. 
                    '''



    def find_idx(self,std_no):
        target_idx = -1 # -1 은 찾는 학생이 없음을 의미

        for i in range(len(self.student_list)):
            if self.student_list[i].std_no == std_no:  # student_list[i]는 학생리스트에 담긴 Student형 instance 변수이다.
                target_idx = i

        return target_idx

    def del_std(self,std_no): #std_no: 사용자에게 입력받은 학번이 들어감
        if self.find_idx(std_no) == -1: #  찾는 학생이 없는 경우
            print("찾는 학생이 없습니다. 초기화면으로 돌아갑니다.")
        else: #찾는 학생이 있는 경우
            print(self.student_list[self.find_idx(std_no)].name, "님이 삭제되었습니다.")
            self.student_list.pop(self.find_idx(std_no))
            # print문을 먼저 안쓰면 pop함수로 정보가 사라졌으니 그 다음 정보의 이름을 반환하겠지요? 바보

    def print_info(self):
        for std in self.student_list:
            std.print_std()

    def print_avg(self):
        grade = [0] * 5
        for i in range(len(self.student_list)):
            for j in range(len(self.student_list[i].grade_dict.values())):
                grade[j] += list(self.student_list[i].grade_dict.values())[j]
                # '+=' 주의하기~!
        korAvg = grade[0] / len(self.student_list)
        maAvg = grade[1] / len(self.student_list)
        enAvg = grade[2] / len(self.student_list)
        soAvg = grade[3] / len(self.student_list)
        scAvg = grade[4] / len(self.student_list)
        allAvg = sum(grade) / (len(self.student_list)*5)  #len(student_list)만 하면 과목수가 반영안되므로 *5 !!!!!

        print("국어평균: ", korAvg ,"|", "수학평균: ", round(maAvg,3) , "|" , "영어평균: ", round(enAvg,3) , "|",
              "사회평균: ", round(soAvg,3) , "|", "과학평균: ", round(scAvg,3) , "|", "전체평균: ", round(allAvg,3))


sms = SMS()   # while True 안에다가 sms = SMS()가 된다면 이는 하나의 flag가 종료되고 다시 돌아갈 때 마다 sms가 초기화되므로 안됨

while True:
    flag = int(input("메뉴를 선택하세요 \n 1. 조회 2. 추가 3. 삭제 4. 종료"))
    if flag == 1:
        if len(sms.student_list) == 0:
            print("학생리스트가 비어있습니다. 초기화면으로 돌아갑니다.")
        else:
            sms.print_info()
            sms.print_avg()
    elif flag == 2:
        name = input("이름을 입력하세요: ")
        std_no = int(input("학번을 입력하세요: "))
        grade = { "국어": int(input("국어점수를 입력하세요: ")),
                  "수학": int(input("수학점수를 입력하세요: ")),
                  "영어": int(input("영어점수를 입력하세요: ")),
                  "사회": int(input("사회점수를 입력하세요: ")),
                  "과학": int(input("과학점수를 입력하세요: "))
                  }
        std = Student(name, std_no, grade)
        sms.insert(std)

    elif flag == 3:
        std_no = int(input("삭제할 학생의 학번을 입력하세요: "))
        sms.del_std(std_no)

    elif flag == 4:
        print("학생 정보관의 시스템을 종료합니다.")
        break



