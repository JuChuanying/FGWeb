function runFontDiffuser() {
    const formData = new FormData();
    formData.append('sourceImage', document.getElementById('sourceImage').files[0]);
    formData.append('referenceImage', document.getElementById('referenceImage').files[0]);

    fetch('/process-images', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(imageBlob => {
        // 显示或处理返回的图像
        const imageObjectURL = URL.createObjectURL(imageBlob);
        console.log(imageObjectURL);
    });
}