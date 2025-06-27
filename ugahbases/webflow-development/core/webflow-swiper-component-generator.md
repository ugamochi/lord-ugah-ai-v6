# Webflow Swiper Component Generator (Merged)

**Note:** This file was merged with `swiper-accessibility-checklist.md` and `swiper-navigation-cleaner.md` (2025-06-26) to consolidate all accessibility, navigation cleaning, and best practices for Swiper.js in Webflow. All valuable content from both sources is preserved below. The original checklist and navigation cleaner files are now archived.

**Created:** 2025-06-26  
**Purpose:** Generate modular, independent Swiper.js components for Webflow projects following Timothy Ricks' architecture patterns

---

## Role Definition

You are a senior frontend developer and Swiper.js expert with extensive experience in component-based architecture, Webflow development, and accessibility implementation. You specialize in creating isolated, reusable components that coexist without conflicts using Timothy Ricks' proven scoping patterns.

## Task Specification

Generate a complete, production-ready Swiper.js component that follows component isolation principles, includes responsive design, accessibility features, and integrates seamlessly with Webflow's design system without styling conflicts.

## Detailed Specifications

### 1. Component Architecture Requirements
- Use IIFE pattern for complete namespace isolation
- Implement component wrapper scoping (`.{component-name}-component`)
- Include existence validation before initialization
- Provide proper cleanup on page unload
- Handle resize events with debouncing (250ms)

### 2. Swiper Configuration Standards
- Single-slide navigation: `slidesPerGroup: 1`, `centeredSlides: false`
- Responsive breakpoints: 320px, 768px, 992px minimum
- Infinite loop with `loopAdditionalSlides: 2`
- Accessibility support with custom screen reader messages
- Error handling with graceful fallbacks

### 3. Navigation & Interaction
- Remove all default Swiper styling completely
- Support multiple interaction methods (touch, mouse, keyboard, mousewheel)
- Custom disabled class to prevent button locking
- Scoped button selectors within component wrapper

### 4. Responsive Design
- Mobile-first approach with progressive enhancement
- Flexible spacing using em units or conditional pixel values
- Configurable slides per view for each breakpoint
- Orientation change handling with 100ms delay

### 5. Accessibility Compliance (WCAG 2.2 AA)
- Meaningful screen reader messages for navigation
- Keyboard navigation support (arrow keys, tab)
- Focus management for dynamic content
- Respect for `prefers-reduced-motion` settings

### 6. Performance Optimization
- Passive event listeners where applicable
- Minimal DOM manipulation
- Efficient selector caching
- No unnecessary feature loading

### 7. Production Readiness
- No console.log statements in final output
- Comprehensive error boundaries
- Graceful degradation for missing elements
- Clean, commented code structure

### 8. Integration Requirements
- Compatible with Webflow's export structure
- No conflicts with existing CSS frameworks
- Support for custom Webflow class names
- Preservation of Webflow's responsive behavior

## Component Template

```javascript
/**
 * {ComponentName} Swiper Component
 * Created: {CURRENT_DATE}
 * 
 * {Brief description of component purpose and behavior}
 * Follows Timothy Ricks' component-based architecture patterns
 * Independent from other swiper components
 */

(function() {
  'use strict';
  
  let swiperInstance = null;
  let resizeTimer;

  function init{ComponentName}Swiper() {
    if (swiperInstance) return;

    // Component scoping - only target this component
    const component = document.querySelector('.{component-class}-component');
    if (!component) return;

    const swiperElement = component.querySelector('.{swiper-class}.swiper');
    if (!swiperElement) return;

    const nextButton = component.querySelector('.swiper-button-next');
    const prevButton = component.querySelector('.swiper-button-prev');

    try {
      swiperInstance = new Swiper(swiperElement, {
        wrapperClass: '{wrapper-class} swiper-wrapper',
        slideClass: '{slide-class}',
        slidesPerView: {base-slides-per-view},
        spaceBetween: '{base-spacing}',
        slidesPerGroup: 1,
        centeredSlides: false,
        loop: true,
        allowTouchMove: true,
        watchOverflow: false,
        followFinger: true,
        freeMode: false,
        slideToClickedSlide: false,
        loopAdditionalSlides: 2,
        mousewheel: {
          forceToAxis: true
        },
        touchRatio: 1,
        touchAngle: 45,
        simulateTouch: true,
        navigation: {
          nextEl: component.querySelector('.swiper-button-next'),
          prevEl: component.querySelector('.swiper-button-prev'),
          disabledClass: 'swiper-button-disabled-DISABLED'
        },
        breakpoints: {
          320: {
            slidesPerView: {mobile-slides},
            spaceBetween: '{mobile-spacing}',
            slidesPerGroup: 1
          },
          768: {
            slidesPerView: {tablet-slides},
            spaceBetween: '{tablet-spacing}',
            slidesPerGroup: 1
          },
          992: {
            slidesPerView: {desktop-slides},
            spaceBetween: '{desktop-spacing}',
            slidesPerGroup: 1
          }
        },
        a11y: {
          enabled: true,
          prevSlideMessage: 'Previous {content-type}',
          nextSlideMessage: 'Next {content-type}',
          firstSlideMessage: 'This is the first {content-type}',
          lastSlideMessage: 'This is the last {content-type}'
        },
        keyboard: {
          enabled: true,
          onlyInViewport: true
        }
      });
      
      // Remove default Swiper styling from navigation buttons
      if (nextButton) {
        Object.assign(nextButton.style, {
          border: 'none', outline: 'none', boxShadow: 'none',
          width: 'auto', height: 'auto', marginTop: '0',
          position: 'static', top: 'auto', right: 'auto',
          left: 'auto', bottom: 'auto', transform: 'none'
        });
        
        const nextStyle = document.createElement('style');
        nextStyle.textContent = `
          .swiper-button-next::after {
            display: none !important;
            content: '' !important;
          }
          .swiper-button-next {
            color: inherit !important;
          }
        `;
        document.head.appendChild(nextStyle);
      }
      
      if (prevButton) {
        Object.assign(prevButton.style, {
          border: 'none', outline: 'none', boxShadow: 'none',
          width: 'auto', height: 'auto', marginTop: '0',
          position: 'static', top: 'auto', right: 'auto',
          left: 'auto', bottom: 'auto', transform: 'none'
        });
        
        const prevStyle = document.createElement('style');
        prevStyle.textContent = `
          .swiper-button-prev::after {
            display: none !important;
            content: '' !important;
          }
          .swiper-button-prev {
            color: inherit !important;
          }
        `;
        document.head.appendChild(prevStyle);
      }
    } catch (error) {
      swiperInstance = null;
    }
  }

  function destroy{ComponentName}Swiper() {
    if (!swiperInstance) return;
    
    try {
      swiperInstance.destroy(true, true);
    } catch (error) {
    } finally {
      swiperInstance = null;
    }
  }

  function handleResize() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
      if (swiperInstance) {
        try {
          swiperInstance.update();
        } catch (error) {
          destroy{ComponentName}Swiper();
          init{ComponentName}Swiper();
        }
      }
    }, 250);
  }

  function init() {
    init{ComponentName}Swiper();
    window.addEventListener('resize', handleResize);
    window.addEventListener('orientationchange', () => {
      setTimeout(handleResize, 100);
    });
  }

  function cleanup() {
    window.removeEventListener('resize', handleResize);
    destroy{ComponentName}Swiper();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.addEventListener('unload', cleanup);

  window.{ComponentName}Swiper = {
    init: init{ComponentName}Swiper,
    destroy: destroy{ComponentName}Swiper,
    getInstance: () => swiperInstance
  };

})();
```

## Usage Instructions

### Required Inputs
1. **Component Name** (PascalCase): e.g., "RelatedPosts", "ProductGallery"
2. **Component Class** (kebab-case): e.g., "related-posts", "product-gallery"
3. **Swiper Class**: Webflow's swiper container class
4. **Wrapper Class**: Webflow's wrapper class name
5. **Slide Class**: Webflow's individual slide class name
6. **Content Type**: For accessibility messages (e.g., "post", "product", "image")

### Responsive Configuration
- **Mobile (320px)**: slides per view, spacing
- **Tablet (768px)**: slides per view, spacing  
- **Desktop (992px)**: slides per view, spacing

### Conditional Behaviors
- **Mobile-only**: Add condition `if (!isMobile()) return;` before component check
- **Desktop-only**: Add condition `if (isMobile()) return;` before component check
- **Custom breakpoints**: Modify breakpoint values as needed

## Examples

### Example 1: Related Posts Swiper
```javascript
// Input: RelatedPosts, related-posts, blogpost-collection-slider, blogpost-slider, blogpost-item, post
// Responsive: 1/2/3 slides, 1.11em/2.22em/3.06em spacing
// Behavior: All screen sizes
```

### Example 2: Mobile-Only Product Gallery
```javascript
// Input: ProductGallery, product-gallery, product-slider, product-wrapper, product-slide, product  
// Responsive: auto/disabled/disabled, 0.5em/0/0 spacing
// Behavior: Mobile-only with breakpoint check
```

## Reference Materials

- @swiper-js-reference-2025.md for API documentation
- @.cursor-rules for Webflow development standards
- Timothy Ricks component architecture patterns
- WCAG 2.2 AA accessibility guidelines

## Response Formatting

Provide the complete JavaScript component with:
1. **Header comment** with component name, date, and description
2. **Configuration object** with all specified parameters
3. **Navigation styling cleanup** for both buttons
4. **Error handling** with graceful fallbacks
5. **Responsive breakpoints** as specified
6. **Accessibility features** with custom messages
7. **Global exposure** for external access if needed

Generate clean, production-ready code that can be directly implemented in Webflow custom code sections. 

---

## Navigation Styling Cleanup (Merged from swiper-navigation-cleaner.md)

// Implementation patterns, JS/CSS code, and rationale for removing Swiper's default navigation styling while preserving Webflow design system integrity.
// See references/swiper-navigation-cleaner.md for full details.

### JavaScript Style Reset Example
```javascript
function cleanSwiperNavigation(button, buttonType) {
  if (!button) return;
  Object.assign(button.style, {
    position: 'static', top: 'auto', right: 'auto', left: 'auto', bottom: 'auto', transform: 'none', zIndex: 'auto', width: 'auto', height: 'auto', margin: '0', marginTop: '0', padding: 'inherit', border: 'none', outline: 'none', boxShadow: 'none', background: 'none', backgroundColor: 'transparent', fontSize: 'inherit', fontFamily: 'inherit', fontWeight: 'inherit', textAlign: 'inherit', cursor: 'inherit', userSelect: 'inherit', pointerEvents: 'inherit'
  });
  // Remove pseudo-element arrows
  const styleId = `swiper-${buttonType}-cleanup`;
  let styleElement = document.getElementById(styleId);
  if (!styleElement) {
    styleElement = document.createElement('style');
    styleElement.id = styleId;
    styleElement.textContent = `
      .swiper-button-${buttonType}::after { display: none !important; content: '' !important; opacity: 0 !important; visibility: hidden !important; }
      .swiper-button-${buttonType} { color: inherit !important; background: none !important; border: none !important; }
    `;
    document.head.appendChild(styleElement);
  }
}
```

### CSS-Only Override Example
```css
.swiper-container .swiper-button-next,
.swiper-container .swiper-button-prev,
div[class*="swiper"] .swiper-button-next,
div[class*="swiper"] .swiper-button-prev {
  position: static !important;
  width: auto !important;
  height: auto !important;
  margin: 0 !important;
  background: none !important;
  border: none !important;
  outline: none !important;
  transform: none !important;
  top: auto !important;
  right: auto !important;
  left: auto !important;
  bottom: auto !important;
  z-index: auto !important;
  color: inherit !important;
}
.swiper-button-next::after,
.swiper-button-prev::after {
  display: none !important;
  content: '' !important;
  opacity: 0 !important;
  visibility: hidden !important;
}
```

---

## Accessibility Checklist & Patterns (Merged from swiper-accessibility-checklist.md)

// Key code patterns, checklists, and best practices for WCAG 2.2 AA compliance, keyboard navigation, focus management, motion preferences, and ARIA implementation.
// See references/swiper-accessibility-checklist.md for full details.

### Screen Reader Messages Example
```javascript
a11y: {
  enabled: true,
  prevSlideMessage: 'Previous {content-type}',
  nextSlideMessage: 'Next {content-type}',
  firstSlideMessage: 'This is the first {content-type}',
  lastSlideMessage: 'This is the last {content-type}',
  paginationBulletMessage: 'Go to {content-type} {{index}}',
  slideLabelMessage: '{{index}} / {{slidesLength}}'
}
```

### Keyboard Navigation Example
```javascript
keyboard: {
  enabled: true,
  onlyInViewport: true,
  pageUpDown: true
}
```

### Focus Management Example
```javascript
swiper.on('slideChange', function() {
  const activeSlide = this.slides[this.activeIndex];
  const focusableElement = activeSlide.querySelector('a, button, [tabindex]:not([tabindex="-1"])');
  if (focusableElement) {
    setTimeout(() => { focusableElement.focus(); }, 300);
  }
});
```

### Motion Preferences Example
```javascript
function respectReducedMotion(swiperConfig) {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion) {
    swiperConfig.autoplay = false;
    swiperConfig.speed = 0;
    swiperConfig.effect = 'slide';
    const style = document.createElement('style');
    style.textContent = `.swiper-slide { transition: none !important; } .swiper-wrapper { transition-duration: 0ms !important; }`;
    document.head.appendChild(style);
  }
  return swiperConfig;
}
```

---

## Reference & Troubleshooting Appendix (Merged from swiper-js-reference-2025.md)

// Unique tips, troubleshooting, and configuration examples for Swiper.js in Webflow. See references/swiper-js-reference-2025.md for full details.

### Common Configurations
```javascript
// Single Slide Navigation
{
  slidesPerView: 1,
  slidesPerGroup: 1,
  centeredSlides: false,
  spaceBetween: 20,
  loop: true
}
// Auto-Width Slides
{
  slidesPerView: 'auto',
  spaceBetween: 20,
  centeredSlides: false
}
```

### Troubleshooting
- Slides not moving one at a time: Set `slidesPerGroup: 1`, ensure `freeMode: false`.
- Navigation buttons not working: Verify selectors, check DOM existence, ensure component scoping.
- Loop not working smoothly: Add `loopAdditionalSlides: 2`, ensure sufficient slides.

---

## Component Architecture Patterns (Reference)

// For foundational patterns, see references/component-architecture-patterns.md and component-architecture-validator.md.
// Patterns include: core isolation, wrapper-based scoping, event handler isolation, error boundaries, and performance optimizations. 

## 6. Performance Optimization
// ... existing performance content ...

// ---
// Reference advanced style override system and performance notes from swiper-navigation-cleaner.md here

// ... rest of the file ... 