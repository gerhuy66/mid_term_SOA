async function getQuestion(examId){
    $.ajax({
        url: "/getQuestion",
        data: {
            eId : examId
        },
        success: function(rs){
            $('#question_table').empty();
           rs.forEach(function(ele){
                 template = `<div style='padding:10px;background-color:#232344;'>
                <div style='width:100%;height:10px;color:white;'>Question ${ele[0].substring(1,2)}: ${ele[1]}</div><br>
                <div style='color:white;'>
                    <form id='answer_option_${ele[0]}'>
                        <input type='radio' name='option_${ele[0]}' value='${ele[2]}'/><label for='option_${ele[0]}'>A. ${ele[2]}</label>
                        <input type='radio' name='option_${ele[0]}' value='${ele[3]}'/><label for='option_${ele[0]}'>B. ${ele[3]}</label>
                        <input type='radio' name='option_${ele[0]}' value='${ele[4]}'/><label for='option_${ele[0]}'>C. ${ele[4]}</label>
                        <input type='radio' name='option_${ele[0]}' value='${ele[5]}'/><label for='option_${ele[0]}'>D. ${ele[5]}</label>
                    </form>
                </div>
            </div>`;
            $("#question_table").append(template);
           })
        },
        dataType: "json"
      });

    return "Success";
}

function hoverSubject(ev){
    // console.log(ev);
    $(ev.currentTarget).css("background-color", "#ff99c2");
}
function subjectMouseOut(ev,color){
    $(ev.currentTarget).css("background-color", color);
    // $(ev.currentTarget).css("width", "80px");
    // $(ev.currentTarget).css("height", "80px");
}
function loadSubject(){
    $.ajax({
        url: "/getSubject",
        success: function(rs){
            rs.forEach(function(line){
                let color = '#'+Math.floor(Math.random()*16777215).toString(16);
                // let textColor = '#'+Math.floor(Math.random()*16777215).toString(16);
                let template = `<div class="subject" onclick="loadExamBySub('${line[0]}')" style="color:black;box-shadow:1px 1px 3px 3px lightblue;text-align:center;display:inline-block;background-color:${color};"><p>${line[1]}</p></div>`;
                $('#subjects').append(template);
            });
        },
        dataType: "json"
    });



}

function loadExamBySub(subjectId){
    $.ajax({
        url:"/getExamsBySub",
        data:{
            subId:subjectId
        },
        success:function(rs){
            $('#exams').empty();
            rs.forEach(function(e){
        
                let color = '#'+Math.floor(Math.random()*16777215).toString(16);
                let template = `<div onclick = 'getQuestion("${e[0]}")' style='width:100%;height:50px;background-color:${color};'>exam: ${e[0]}, duration: ${e[1]}</div>`;
                $('#exams').append(template);

            });
        },
        dataType:"json"
    });
}

function initView(){
    loadSubject();
}