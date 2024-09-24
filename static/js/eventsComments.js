const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_content");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteCommentButtons = document.getElementsByClassName("btn-delete-comment");
// different delete classes for the 2 different delete modals
const deleteConfirm = document.getElementById("deleteConfirm");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

const deleteEventButtons = document.getElementsByClassName("btn-delete-event");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText; 
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

for (let button of deleteCommentButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}

// event delete
for (let button of deleteEventButtons) {
  button.addEventListener("click", (e) => {
      // Prevent default action
      e.preventDefault();

      // Get the event ID and slug from the button's data attributes
      let eventId = e.target.getAttribute("data-event-id");
      let eventSlug = e.target.getAttribute("data-event-slug");

      // Set the href of the delete confirmation button inside the modal
      let deleteEventConfirm = document.getElementById("deleteEventConfirm");
      deleteEventConfirm.href = `/event/${eventSlug}/delete_event/${eventId}`;

      // Show the delete confirmation modal for events
      let deleteEventModal = new bootstrap.Modal(document.getElementById('deleteEventModal'));
      deleteEventModal.show();
  });
}
