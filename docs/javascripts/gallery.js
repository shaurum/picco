const gallerySets = {
    'gallery1': [
        'img/inistallation/inistallation_1_1.svg',    // без буквы m
        'img/inistallation/inistallation_1_2.svg',    // без буквы m
        'img/inistallation/inistallation_1_3.svg',    // без буквы m
    ],
};

let currentImages = [];
let currentIndex = 0;
let currentGallery = '';
let scrollPosition = 0;

function openGallery(index, galleryId) {
    // Save scroll position
    scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
    
    currentIndex = index;
    currentGallery = galleryId;
    currentImages = gallerySets[galleryId] || [];
    
    const modal = document.getElementById('galleryModal');
    const galleryImage = document.getElementById('galleryImage');
    const imageCounter = document.getElementById('imageCounter');
    
    if (currentImages.length > 0) {
        galleryImage.src = currentImages[currentIndex];
        imageCounter.textContent = `${currentIndex + 1} / ${currentImages.length}`;
        modal.style.display = 'block';
        // Lock body scroll
        document.body.style.overflow = 'hidden';
        document.body.style.position = 'fixed';
        document.body.style.top = `-${scrollPosition}px`;
        document.body.style.width = '100%';
    }
}

function closeGallery() {
    const modal = document.getElementById('galleryModal');
    modal.style.display = 'none';
    
    // Restore scroll and position
    document.body.style.overflow = '';
    document.body.style.position = '';
    document.body.style.top = '';
    document.body.style.width = '';
    window.scrollTo(0, scrollPosition);
    
    currentImages = [];
    currentGallery = '';
}

function prevImage() {
    if (currentImages.length > 0) {
        currentIndex = (currentIndex - 1 + currentImages.length) % currentImages.length;
        updateGallery();
    }
}

function nextImage() {
    if (currentImages.length > 0) {
        currentIndex = (currentIndex + 1) % currentImages.length;
        updateGallery();
    }
}

function updateGallery() {
    const galleryImage = document.getElementById('galleryImage');
    const imageCounter = document.getElementById('imageCounter');
    
    if (currentImages.length > 0) {
        galleryImage.src = currentImages[currentIndex];
        imageCounter.textContent = `${currentIndex + 1} / ${currentImages.length}`;
    }
}

// Keyboard controls
document.addEventListener('keydown', function(e) {
    const modal = document.getElementById('galleryModal');
    if (modal.style.display === 'block') {
        if (e.key === 'Escape') {
            closeGallery();
        } else if (e.key === 'ArrowLeft') {
            prevImage();
        } else if (e.key === 'ArrowRight') {
            nextImage();
        }
    }
});

// Close on background or image click
document.getElementById('galleryModal').addEventListener('click', function(e) {
    if (e.target === this || e.target.id === 'galleryImage') {
        closeGallery();
    }
});