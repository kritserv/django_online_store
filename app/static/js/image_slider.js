const sliderMainImage = document.getElementById("product-main-image");
const sliderImageList = document.getElementsByClassName("image-list");

for (let i = 0; i < sliderImageList.length; i++) {
    sliderImageList[i].onclick = function () {
        sliderMainImage.src = this.src;
    };
}
