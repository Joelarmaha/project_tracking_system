// Example JS file for future features
console.log("Project Tracking System frontend loaded.");

// Optional: confirm before delete
document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll("a.btn-danger");
    deleteButtons.forEach(btn => {
        btn.addEventListener("click", function(e) {
            if (!confirm("Are you sure you want to delete this item?")) {
                e.preventDefault();
            }
        });
    });
});
