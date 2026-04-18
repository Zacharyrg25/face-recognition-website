const input = document.getElementById('imageInput');
const detect = document.getElementById('detectBtn');
const canvas = document.getElementById('canvas');
const status = document.getElementById('status');
const ctx = canvas.getContext('2d');

input.addEventListener('change', () => {
    const file = input.files[0];
    const img = new Image();
    img.src = URL.createObjectURL(file);
    img.onload = () => {
        canvas.hidden = false;
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);
        status.textContent = `Image loaded!`;
        canvas.style.border = "1px solid hsl(0, 0%, 15%)";
    }
});

detect.addEventListener('click', () => {
    let checkedInput = document.querySelector('input[name="mode"]:checked'); // NEW NEW NEW
    const file = input.files[0];
    if (!file) {
        status.textContent = 'Please select an image first!';
        return;
    }

    // Show the image on the canvas first
    const img = new Image();
    img.src = URL.createObjectURL(file);
    img.onload = () => {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);
        status.textContent = 'Detecting faces...';

        // Send the image to Flask
        const formData = new FormData();
        formData.append('image', file);
        formData.append('mode', checkedInput.value);

        fetch('/detect', {
            method: 'POST',
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            // Draw a red box around each face
            ctx.strokeStyle = 'red';
            ctx.lineWidth = 3;
            data.faces.forEach(face => {
                ctx.strokeRect(face.x, face.y, face.w, face.h);
            });

            // Show how many faces were found
            if (data.faces.length === 0) {
                status.textContent = 'No faces detected. Try a different image!';
            } else {
                status.textContent = `Detected ${data.faces.length} face(s) using the ${checkedInput.value} method!`;
            }
        })
        .catch(() => {
            status.textContent = 'Something went wrong!';
        });
    };
});