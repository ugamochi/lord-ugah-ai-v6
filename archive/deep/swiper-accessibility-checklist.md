# Swiper Accessibility Checklist

**Created:** 2025-06-26  
**Purpose:** Comprehensive accessibility implementation guide for Swiper.js components in Webflow projects

---

## WCAG 2.2 AA Compliance Standards

### Core Requirements
- Screen reader compatibility with meaningful messages
- Keyboard navigation support (arrow keys, tab navigation)
- Focus management for dynamic content
- Motion preferences respect (`prefers-reduced-motion`)
- Touch target minimum sizes (44px × 44px)

## Screen Reader Implementation

### Custom Screen Reader Messages
```javascript
// Context-specific accessibility messages
a11y: {
  enabled: true,
  prevSlideMessage: 'Previous {content-type}',
  nextSlideMessage: 'Next {content-type}',
  firstSlideMessage: 'This is the first {content-type}',
  lastSlideMessage: 'This is the last {content-type}',
  paginationBulletMessage: 'Go to {content-type} {{index}}',
  slideLabelMessage: '{{index}} / {{slidesLength}}'
}

// Examples for different content types:
// Blog posts: "Previous blog post", "Next blog post"
// Products: "Previous product", "Next product" 
// Images: "Previous image", "Next image"
// Testimonials: "Previous testimonial", "Next testimonial"
```

### Advanced Screen Reader Configuration
```javascript
// Enhanced accessibility setup
a11y: {
  enabled: true,
  containerMessage: 'Interactive content slider',
  containerRole: 'region',
  containerRoleDescriptionMessage: 'Carousel of {content-type}s',
  itemRoleDescriptionMessage: '{content-type} slide',
  slideRole: 'group',
  prevSlideMessage: 'Previous {content-type}',
  nextSlideMessage: 'Next {content-type}',
  firstSlideMessage: 'This is the first {content-type}',
  lastSlideMessage: 'This is the last {content-type}',
  paginationBulletMessage: 'Go to {content-type} {{index}}',
  slideLabelMessage: '{content-type} {{index}} of {{slidesLength}}',
  notificationClass: 'swiper-notification',
  scrollOnFocus: true
}
```

## Keyboard Navigation

### Standard Keyboard Support
```javascript
// Enable comprehensive keyboard navigation
keyboard: {
  enabled: true,
  onlyInViewport: true,
  pageUpDown: true
}

// Supported keyboard interactions:
// - Arrow Left/Right: Navigate slides
// - Arrow Up/Down: Navigate slides (if pageUpDown: true)
// - Tab: Focus navigation elements
// - Enter/Space: Activate buttons
// - Escape: Exit full-screen or modal modes
```

### Custom Keyboard Handlers
```javascript
// Enhanced keyboard navigation with custom handlers
function enhanceKeyboardNavigation(swiper, component) {
  const swiperElement = component.querySelector('.swiper');
  
  if (swiperElement) {
    swiperElement.addEventListener('keydown', (event) => {
      switch (event.key) {
        case 'Home':
          event.preventDefault();
          swiper.slideTo(0);
          break;
        case 'End':
          event.preventDefault();
          swiper.slideTo(swiper.slides.length - 1);
          break;
        case 'PageUp':
          event.preventDefault();
          swiper.slidePrev();
          break;
        case 'PageDown':
          event.preventDefault();
          swiper.slideNext();
          break;
      }
    });
  }
}
```

## Focus Management

### Proper Focus Handling
```javascript
// Focus management for dynamic content
swiper.on('slideChange', function() {
  const activeSlide = this.slides[this.activeIndex];
  const focusableElement = activeSlide.querySelector('a, button, [tabindex]:not([tabindex="-1"])');
  
  if (focusableElement) {
    // Delay focus to ensure smooth transition
    setTimeout(() => {
      focusableElement.focus();
    }, 300);
  }
});

// Ensure proper focus outline visibility
swiper.on('init', function() {
  const navigationButtons = component.querySelectorAll('.swiper-button-next, .swiper-button-prev');
  navigationButtons.forEach(button => {
    button.style.outline = 'none'; // Remove default outline
    button.addEventListener('focus', () => {
      button.style.boxShadow = '0 0 0 2px #005fcc'; // Custom focus indicator
    });
    button.addEventListener('blur', () => {
      button.style.boxShadow = 'none';
    });
  });
});
```

### Skip Navigation Support
```javascript
// Add skip navigation for screen readers
function addSkipNavigation(component) {
  const skipButton = document.createElement('button');
  skipButton.className = 'skip-slider';
  skipButton.textContent = 'Skip slider navigation';
  skipButton.style.cssText = `
    position: absolute;
    left: -9999px;
    width: 1px;
    height: 1px;
    overflow: hidden;
  `;
  
  skipButton.addEventListener('focus', () => {
    skipButton.style.cssText = `
      position: absolute;
      top: 0;
      left: 0;
      z-index: 1000;
      padding: 8px 12px;
      background: #000;
      color: #fff;
      text-decoration: none;
    `;
  });
  
  skipButton.addEventListener('blur', () => {
    skipButton.style.cssText = `
      position: absolute;
      left: -9999px;
      width: 1px;
      height: 1px;
      overflow: hidden;
    `;
  });
  
  skipButton.addEventListener('click', () => {
    const nextElement = component.nextElementSibling;
    if (nextElement) {
      nextElement.focus();
    }
  });
  
  component.insertBefore(skipButton, component.firstChild);
}
```

## Motion Preferences

### Respect Reduced Motion Settings
```javascript
// Check for reduced motion preference
function respectReducedMotion(swiperConfig) {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  if (prefersReducedMotion) {
    // Disable auto-transitions and reduce animation speed
    swiperConfig.autoplay = false;
    swiperConfig.speed = 0;
    swiperConfig.effect = 'slide'; // Force slide effect (no fancy transitions)
    
    // Remove any CSS transitions from slides
    const style = document.createElement('style');
    style.textContent = `
      .swiper-slide {
        transition: none !important;
      }
      .swiper-wrapper {
        transition-duration: 0ms !important;
      }
    `;
    document.head.appendChild(style);
  }
  
  return swiperConfig;
}

// Usage in component initialization
let swiperConfig = {
  speed: 400,
  autoplay: {
    delay: 3000
  },
  // ... other config
};

swiperConfig = respectReducedMotion(swiperConfig);
const swiper = new Swiper(element, swiperConfig);
```

### Dynamic Motion Preference Updates
```javascript
// Listen for motion preference changes
function setupMotionPreferenceListener(swiper) {
  const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  
  function handleMotionPreferenceChange(e) {
    if (e.matches) {
      // User now prefers reduced motion
      if (swiper.autoplay) {
        swiper.autoplay.stop();
      }
      swiper.params.speed = 0;
    } else {
      // User no longer prefers reduced motion
      swiper.params.speed = 400;
      if (swiper.params.autoplay) {
        swiper.autoplay.start();
      }
    }
  }
  
  mediaQuery.addEventListener('change', handleMotionPreferenceChange);
  
  // Cleanup
  return () => {
    mediaQuery.removeEventListener('change', handleMotionPreferenceChange);
  };
}
```

## Touch Target Guidelines

### Minimum Touch Target Sizes
```css
/* Ensure adequate touch targets (44px minimum) */
.swiper-button-next,
.swiper-button-prev {
  min-width: 44px;
  min-height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.swiper-pagination-bullet {
  min-width: 44px;
  min-height: 44px;
  border-radius: 50%;
}

/* For smaller visual buttons, extend the touch area */
.small-nav-button {
  position: relative;
}

.small-nav-button::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  min-width: 44px;
  min-height: 44px;
  z-index: -1;
}
```

### Touch Gesture Accessibility
```javascript
// Enhanced touch accessibility
touchRatio: 1,
touchAngle: 45,
touchStartPreventDefault: false,
touchMoveStopPropagation: false,
simulateTouch: true,
allowTouchMove: true,

// Long press gesture support
longSwipesRatio: 0.5,
longSwipesMs: 300,

// Resistance for better haptic feedback
resistance: true,
resistanceRatio: 0.85
```

## ARIA Implementation

### Complete ARIA Setup
```javascript
// Enhanced ARIA attributes
swiper.on('init', function() {
  const swiperContainer = this.el;
  const slides = this.slides;
  const wrapper = swiperContainer.querySelector('.swiper-wrapper');
  
  // Container ARIA attributes
  swiperContainer.setAttribute('role', 'region');
  swiperContainer.setAttribute('aria-label', 'Image carousel');
  swiperContainer.setAttribute('aria-roledescription', 'carousel');
  
  // Wrapper ARIA attributes
  wrapper.setAttribute('role', 'group');
  wrapper.setAttribute('aria-live', 'polite');
  wrapper.setAttribute('aria-atomic', 'false');
  
  // Slide ARIA attributes
  slides.forEach((slide, index) => {
    slide.setAttribute('role', 'group');
    slide.setAttribute('aria-roledescription', 'slide');
    slide.setAttribute('aria-label', `Slide ${index + 1} of ${slides.length}`);
    
    // Hide inactive slides from screen readers
    if (index !== this.activeIndex) {
      slide.setAttribute('aria-hidden', 'true');
    }
  });
  
  // Navigation button ARIA attributes
  const nextButton = swiperContainer.querySelector('.swiper-button-next');
  const prevButton = swiperContainer.querySelector('.swiper-button-prev');
  
  if (nextButton) {
    nextButton.setAttribute('role', 'button');
    nextButton.setAttribute('aria-label', 'Next slide');
    nextButton.setAttribute('tabindex', '0');
  }
  
  if (prevButton) {
    prevButton.setAttribute('role', 'button');
    prevButton.setAttribute('aria-label', 'Previous slide');
    prevButton.setAttribute('tabindex', '0');
  }
});

// Update ARIA attributes on slide change
swiper.on('slideChange', function() {
  this.slides.forEach((slide, index) => {
    if (index === this.activeIndex) {
      slide.setAttribute('aria-hidden', 'false');
      slide.removeAttribute('tabindex');
    } else {
      slide.setAttribute('aria-hidden', 'true');
      slide.setAttribute('tabindex', '-1');
    }
  });
  
  // Announce slide change to screen readers
  const wrapper = this.el.querySelector('.swiper-wrapper');
  wrapper.setAttribute('aria-live', 'assertive');
  setTimeout(() => {
    wrapper.setAttribute('aria-live', 'polite');
  }, 1000);
});
```

## Color and Contrast

### High Contrast Support
```css
/* High contrast mode support */
@media (prefers-contrast: high) {
  .swiper-button-next,
  .swiper-button-prev {
    background: ButtonFace;
    border: 2px solid ButtonText;
    color: ButtonText;
  }
  
  .swiper-button-next:hover,
  .swiper-button-prev:hover {
    background: Highlight;
    color: HighlightText;
  }
  
  .swiper-button-next:focus,
  .swiper-button-prev:focus {
    outline: 2px solid ButtonText;
    outline-offset: 2px;
  }
}

/* Ensure sufficient color contrast (4.5:1 minimum) */
.swiper-button-next,
.swiper-button-prev {
  color: #000;
  background: rgba(255, 255, 255, 0.9);
}

.swiper-button-next:hover,
.swiper-button-prev:hover {
  background: rgba(255, 255, 255, 1);
}
```

## Testing Checklist

### Manual Testing Steps
1. **Screen Reader Testing**
   - [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (Mac)
   - [ ] Verify meaningful announcements for navigation
   - [ ] Check slide content is properly announced
   - [ ] Validate button labels are descriptive

2. **Keyboard Navigation Testing**
   - [ ] Tab through all interactive elements
   - [ ] Use arrow keys to navigate slides
   - [ ] Test Home/End key functionality
   - [ ] Verify focus indicators are visible
   - [ ] Check focus doesn't get trapped

3. **Motion Testing**
   - [ ] Enable "Reduce motion" in system settings
   - [ ] Verify autoplay stops
   - [ ] Check transitions are disabled/minimized
   - [ ] Test with animation-heavy configurations

4. **Touch Target Testing**
   - [ ] Verify buttons are at least 44px × 44px
   - [ ] Test on actual touch devices
   - [ ] Check spacing between interactive elements
   - [ ] Validate gesture responsiveness

### Automated Testing Tools
```javascript
// Accessibility testing helper
function runAccessibilityChecks(swiperElement) {
  const issues = [];
  
  // Check for proper ARIA labels
  const buttons = swiperElement.querySelectorAll('.swiper-button-next, .swiper-button-prev');
  buttons.forEach(button => {
    if (!button.getAttribute('aria-label')) {
      issues.push(`Navigation button missing aria-label: ${button.className}`);
    }
  });
  
  // Check touch target sizes
  buttons.forEach(button => {
    const rect = button.getBoundingClientRect();
    if (rect.width < 44 || rect.height < 44) {
      issues.push(`Touch target too small: ${button.className} (${rect.width}×${rect.height})`);
    }
  });
  
  // Check color contrast (simplified)
  const computedStyle = window.getComputedStyle(buttons[0]);
  const backgroundColor = computedStyle.backgroundColor;
  const color = computedStyle.color;
  
  // Color contrast checking would require a proper contrast calculation
  // This is a placeholder for demonstration
  
  return issues;
}
```

## Implementation Example

### Complete Accessible Swiper Setup
```javascript
function createAccessibleSwiper(component) {
  const swiperElement = component.querySelector('.swiper');
  if (!swiperElement) return;
  
  // Base configuration with accessibility
  let config = {
    // Core accessibility
    a11y: {
      enabled: true,
      prevSlideMessage: 'Previous item',
      nextSlideMessage: 'Next item',
      firstSlideMessage: 'This is the first item',
      lastSlideMessage: 'This is the last item',
      paginationBulletMessage: 'Go to item {{index}}',
      slideLabelMessage: 'Item {{index}} of {{slidesLength}}',
      containerMessage: 'Interactive content slider',
      containerRole: 'region',
      slideRole: 'group'
    },
    
    // Keyboard navigation
    keyboard: {
      enabled: true,
      onlyInViewport: true,
      pageUpDown: true
    },
    
    // Base settings
    slidesPerView: 1,
    spaceBetween: 20,
    loop: true,
    
    // Navigation
    navigation: {
      nextEl: component.querySelector('.swiper-button-next'),
      prevEl: component.querySelector('.swiper-button-prev')
    }
  };
  
  // Apply motion preferences
  config = respectReducedMotion(config);
  
  // Create swiper instance
  const swiper = new Swiper(swiperElement, config);
  
  // Setup additional accessibility features
  setupMotionPreferenceListener(swiper);
  enhanceKeyboardNavigation(swiper, component);
  addSkipNavigation(component);
  
  // Run accessibility validation
  const issues = runAccessibilityChecks(swiperElement);
  if (issues.length > 0) {
    console.warn('Accessibility issues found:', issues);
  }
  
  return swiper;
}
```

This comprehensive accessibility implementation ensures your Swiper components meet WCAG 2.2 AA standards and provide an excellent experience for all users. 