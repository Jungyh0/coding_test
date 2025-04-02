import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        List<Integer> list = new ArrayList<>();
        student s1 = new student(new int[]{1, 2, 3, 4, 5});
        student s2 = new student(new int[]{2, 1, 2, 3, 2, 4, 2, 5});
        student s3 = new student(new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5});
        
        for (int i = 0; i < answers.length; i ++){
            if (answers[i] == s1.students_answers[i % s1.students_answers.length]){  
                s1.correct_answer ++;
            }
            if (answers[i] == s2.students_answers[i % s2.students_answers.length]){  
                s2.correct_answer ++;
            }
            if (answers[i] == s3.students_answers[i % s3.students_answers.length]){  
                s3.correct_answer ++;
            }
        }
        int max_score = Math.max(s1.correct_answer, Math.max(s2.correct_answer, s3.correct_answer));
        
        if (s1.correct_answer == max_score) list.add(1);
        if (s2.correct_answer == max_score) list.add(2);
        if (s3.correct_answer == max_score) list.add(3);
        
        return list.stream().mapToInt(i -> i).toArray();
    }
}

class student{
    int[] students_answers;
    int correct_answer;
    
    student(int[] answers){
        this.students_answers = answers;
        this.correct_answer = 0;
    }
}