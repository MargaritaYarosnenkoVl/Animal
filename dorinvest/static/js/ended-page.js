document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.ended-page_show').forEach(function (showBlock) {
        showBlock.addEventListener('click', function () {
            var description = this.parentNode.querySelector('.ended-page_show_description');
            if (description.style.height) {
                description.style.height = null;
            } else {
                const height = (description.scrollHeight + 50) + "px";
                description.style.height = height;
            }
            description.classList.toggle('active');

            var rotateButton = this.querySelector('.ended-page_rotate_button img');
            rotateButton.classList.toggle('rotated');
        });
    });
});