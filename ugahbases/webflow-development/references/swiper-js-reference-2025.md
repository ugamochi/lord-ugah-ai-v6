# Swiper.js Reference 2025

## Quick Setup for Webflow

### Basic HTML Structure
```html
<!-- Slider main container -->
<div class="swiper">
  <!-- Additional required wrapper -->
  <div class="swiper-wrapper">
    <!-- Slides -->
    <div class="swiper-slide">Slide 1</div>
    <div class="swiper-slide">Slide 2</div>
    <div class="swiper-slide">Slide 3</div>
  </div>
  <!-- Navigation buttons -->
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
  <!-- Pagination -->
  <div class="swiper-pagination"></div>
</div>
```

### Basic JavaScript Initialization
```javascript
const swiper = new Swiper('.swiper', {
  speed: 400,
  spaceBetween: 100,
});
```

## Core Parameters for Webflow Projects

### Slide Control
- `slidesPerView: 'auto'` - Automatic width based on content
- `slidesPerView: 1` - One slide at a time
- `slidesPerGroup: 1` - Move one slide per navigation
- `centeredSlides: false` - Left-align slides (default)

### Spacing & Layout
- `spaceBetween: 16` - Space between slides in pixels
- `spaceBetween: '1em'` - Space in em units (responsive)

### Navigation
```javascript
navigation: {
  nextEl: '.swiper-button-next',
  prevEl: '.swiper-button-prev',
  disabledClass: 'swiper-button-disabled'
}
```

### Loop & Infinite Scroll
- `loop: true` - Enable infinite loop
- `loopAdditionalSlides: 2` - Extra slides for smooth looping

### Responsive Breakpoints
```javascript
breakpoints: {
  320: {
    slidesPerView: 1,
    spaceBetween: 16
  },
  768: {
    slidesPerView: 2,
    spaceBetween: 24
  },
  992: {
    slidesPerView: 3,
    spaceBetween: 32
  }
}
```

## Interaction Methods

### Touch & Mouse
- `allowTouchMove: true` - Enable touch/swipe
- `touchRatio: 1` - Touch sensitivity
- `simulateTouch: true` - Mouse drag on desktop

### Mouse Wheel
```javascript
mousewheel: {
  forceToAxis: true
}
```

### Keyboard Navigation
```javascript
keyboard: {
  enabled: true,
  onlyInViewport: true
}
```

## Accessibility (A11y)
```javascript
a11y: {
  enabled: true,
  prevSlideMessage: 'Previous slide',
  nextSlideMessage: 'Next slide',
  firstSlideMessage: 'This is the first slide',
  lastSlideMessage: 'This is the last slide'
}
```

## Component Architecture Pattern (Timothy Ricks Style)

### Component Scoping
```javascript
(function() {
  let swiperInstance = null;
  
  function initSwiper() {
    // Component scoping - target specific wrapper
    const component = document.querySelector('.my-swiper-component');
    if (!component) return;
    
    const swiperElement = component.querySelector('.swiper');
    if (!swiperElement) return;
    
    swiperInstance = new Swiper(swiperElement, {
      // Configuration
    });
  }
  
  // Initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSwiper);
  } else {
    initSwiper();
  }
})();
```

## CSS Classes Reference

### Core Classes
- `.swiper` - Main container
- `.swiper-wrapper` - Slides wrapper
- `.swiper-slide` - Individual slide

### Navigation Classes
- `.swiper-button-next` - Next button
- `.swiper-button-prev` - Previous button
- `.swiper-button-disabled` - Disabled state

### Pagination Classes
- `.swiper-pagination` - Pagination container
- `.swiper-pagination-bullet` - Individual bullet
- `.swiper-pagination-bullet-active` - Active bullet

## Webflow-Specific Tips

### Custom Class Names
When using Webflow's custom classes, specify them in initialization:
```javascript
new Swiper('.my-slider', {
  wrapperClass: 'my-wrapper',
  slideClass: 'my-slide'
});
```

### Removing Default Styles
```javascript
// Remove Swiper's default button styling
if (nextButton) {
  nextButton.style.background = 'none';
  nextButton.style.border = 'none';
  
  // Remove pseudo-element arrows
  const style = document.createElement('style');
  style.textContent = `
    .swiper-button-next::after {
      display: none !important;
    }
  `;
  document.head.appendChild(style);
}
```

## Common Configurations

### Single Slide Navigation (Left-Aligned)
```javascript
{
  slidesPerView: 1,
  slidesPerGroup: 1,
  centeredSlides: false,
  spaceBetween: 20,
  loop: true
}
```

### Auto-Width Slides
```javascript
{
  slidesPerView: 'auto',
  spaceBetween: 20,
  centeredSlides: false
}
```

### Responsive Card Grid
```javascript
{
  slidesPerView: 1,
  spaceBetween: 16,
  breakpoints: {
    768: {
      slidesPerView: 2,
      spaceBetween: 24
    },
    992: {
      slidesPerView: 3,
      spaceBetween: 32
    }
  }
}
```

## Troubleshooting

### Slides Not Moving One at a Time
- Set `slidesPerGroup: 1`
- Ensure `freeMode: false`

### Slides Not Left-Aligned
- Set `centeredSlides: false`
- Check CSS for text-align or justify-content

### Navigation Buttons Not Working
- Verify correct selectors in navigation config
- Check if buttons exist in DOM when initializing
- Ensure component scoping is correct

### Loop Not Working Smoothly
- Add `loopAdditionalSlides: 2`
- Ensure sufficient slides for loop

## Performance Tips

### Lazy Loading
```javascript
{
  lazy: true,
  lazy: {
    loadPrevNext: true,
  }
}
```

### Disable Unused Features
```javascript
{
  watchOverflow: false,
  observer: false,
  observeParents: false
}
```

## Documentation Reference
- Official API: https://swiperjs.com/swiper-api
- Version: 11.2.8 (Current as of June 26, 2025)
- All classes and methods fully documented at official site 