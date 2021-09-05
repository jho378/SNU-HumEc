const commentUpdate = (id) => {
    let updateButton = document.querySelector(`.update-${id}`);
    let deleteButton = document.querySelector(`.delete-${id}`);
    let submitButton = document.querySelector(`.submit-${id}`);
    let cancelButton = document.querySelector(`.cancel-${id}`);
    let contents = document.querySelector(`.contents-${id}`);

    console.log(updateButton);
    updateButton.style.display = "none";
    deleteButton.style.display = "none";
    submitButton.style.display = "inline-block";
    cancelButton.style.display = "inline-block";
    contents.readOnly = false;  // 댓글 내용 수정 가능 상태로 변경
}

const handleSuccess = (id) => {
    let updateButton = document.querySelector(`.update-${id}`);
    let deleteButton = document.querySelector(`.delete-${id}`);
    let submitButton = document.querySelector(`.submit-${id}`);
    let cancelButton = document.querySelector(`.cancel-${id}`);
    let contents = document.querySelector(`.contents-${id}`);

    updateButton.style.display = "inline-block";
    deleteButton.style.display = "inline-block";
    submitButton.style.display = "none";
    cancelButton.style.display = "none";
    contents.readOnly = true;
}

const commentUpdateSubmit = (id) => {
    let contents = document.querySelector(`.contents-${id}`).value;
    let param = {
        "id": id,
        "contents": contents,
    }

    $.ajax({
        url: updateUrl,
        type: "POST",
        headers: {"X-CSRFTOKEN": token},
        data: JSON.stringify(param),

        success: function (data) {
            console.log(data);
            if (data.result === "SUCCESS") {
                handleSuccess(id);
            }
        },
        error: function () {
            alert("FAIL");
        }
    })
}

const commentDelete = (id) => {
    let param = {"id": id}
    $.ajax({
        url: deleteUrl,
        type: "POST",
        headers: {"X-CSRFTOKEN": token},
        data: JSON.stringify(param),

        success: function (data) {
            if (data.result === "SUCCESS") {
                let comment = document.querySelector(`.comment-${id}`);
                comment.remove();
            }
        },
        error: function () {
            alert("FAIL");
        }
    })
}