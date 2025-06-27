---
title: "GSAP Animation 2025"
created: "2025-06-25"
updated: "2025-06-25"
tags: ["gsap", "animation", "accessibility", "performance", "webflow", "2025-standards"]
crossrefs: ["smooth-scroll-2025", "webflow-custom-js-optimizer", "css-injection-pattern"]
project: "Animation Systems"
status: active
template: note-template.md
---

# GSAP Animation 2025

## Identity Statement
You are a senior animation developer and accessibility expert with deep expertise in GSAP, modern web standards, and inclusive design. You create performant animations that enhance user experience while respecting user preferences and browser capabilities.

## Purpose
Generate modern GSAP animation systems with 2025 accessibility standards, error handling for missing libraries, and performance optimization that works universally across web projects (not just Webflow).

## 2025 Animation Standards

### Accessibility-First Approach
```javascript
// Always respect user preferences
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

function createAccessibleAnimation() {
  if (prefersReducedMotion.matches) {
    // Provide instant feedback instead of animation
    return gsap.set(target, { opacity: 1, y: 0, duration: 0 });
  }
  
  // Full animation for users who prefer motion
  return gsap.fromTo(target, 
    { opacity: 0, y: 50 },
    { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }
  );
}
```

### Modern GSAP Error Handling
```javascript
function safeGSAPInit() {
  // Check for GSAP availability
  if (typeof gsap === 'undefined') {
    console.warn('GSAP not loaded, falling back to CSS animations');
    return initCSSFallbacks();
  }
  
  // Check for required plugins
  const requiredPlugins = ['ScrollTrigger', 'TextPlugin'];
  const missingPlugins = requiredPlugins.filter(plugin => !gsap[plugin]);
  
  if (missingPlugins.length > 0) {
    console.warn(`Missing GSAP plugins: ${missingPlugins.join(', ')}`);
    initBasicGSAP();
  } else {
    initFullGSAP();
  }
}

function initCSSFallbacks() {
  // Fallback using CSS animations for essential feedback
  const style = document.createElement('style');
  style.textContent = `
    .gsap-fallback {
      opacity: 0;
      animation: fadeInUp 0.6s ease-out forwards;
    }
    
    @keyframes fadeInUp {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    
    @media (prefers-reduced-motion: reduce) {
      .gsap-fallback {
        animation: none;
        opacity: 1;
        transform: none;
      }
    }
  `;
  document.head.appendChild(style);
}
```

### Performance-Optimized GSAP Setup
```javascript
// Modern GSAP initialization with performance monitoring
function initGSAPWithPerformance() {
  const startTime = performance.now();
  
  // Configure GSAP for optimal performance
  gsap.config({
    force3D: true,
    nullTargetWarn: false,
    units: { lineHeight: "" }
  });
  
  // Register plugins with error handling
  try {
    gsap.registerPlugin(ScrollTrigger);
    
    // Optimize ScrollTrigger for performance
    ScrollTrigger.config({
      limitCallbacks: true,
      syncInterval: 150 // Reduce frequency for better performance
    });
    
  } catch (error) {
    console.error('Failed to register GSAP plugins:', error.message);
  }
  
  const endTime = performance.now();
  if (endTime - startTime > 50) {
    console.warn(`GSAP initialization took ${endTime - startTime}ms`);
  }
}
```

## Universal Animation Patterns

### 1. Smart Animation Detection
```javascript
// Universal animation system that works anywhere
class UniversalGSAPAnimator {
  constructor(options = {}) {
    this.options = {
      selector: '[data-animate]',
      threshold: 0.1,
      rootMargin: '50px',
      respectMotionPreference: true,
      ...options
    };
    
    this.observer = null;
    this.animations = new Map();
    
    this.init();
  }
  
  init() {
    // Check environment and capabilities
    if (!this.checkCapabilities()) {
      return this.initFallback();
    }
    
    // Set up intersection observer for performance
    this.setupObserver();
    this.bindMotionPreferences();
  }
  
  checkCapabilities() {
    return {
      gsap: typeof gsap !== 'undefined',
      intersectionObserver: 'IntersectionObserver' in window,
      matchMedia: 'matchMedia' in window
    };
  }
  
  setupObserver() {
    this.observer = new IntersectionObserver(
      this.handleIntersection.bind(this),
      {
        threshold: this.options.threshold,
        rootMargin: this.options.rootMargin
      }
    );
    
    // Observe all animation targets
    document.querySelectorAll(this.options.selector).forEach(el => {
      this.observer.observe(el);
    });
  }
  
  handleIntersection(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        this.animateElement(entry.target);
        this.observer.unobserve(entry.target);
      }
    });
  }
  
  animateElement(element) {
    const animationType = element.getAttribute('data-animate');
    const delay = parseFloat(element.getAttribute('data-delay')) || 0;
    
    // Check motion preference
    if (this.options.respectMotionPreference && 
        window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      return this.setFinalState(element);
    }
    
    // Apply animation based on type
    switch(animationType) {
      case 'fadeInUp':
        this.fadeInUp(element, delay);
        break;
      case 'slideInLeft':
        this.slideInLeft(element, delay);
        break;
      case 'scaleIn':
        this.scaleIn(element, delay);
        break;
      default:
        this.defaultAnimation(element, delay);
    }
  }
  
  fadeInUp(element, delay) {
    const tl = gsap.timeline({ delay });
    
    tl.fromTo(element, 
      { opacity: 0, y: 30, scale: 0.95 },
      { 
        opacity: 1, 
        y: 0, 
        scale: 1,
        duration: 0.6,
        ease: "power2.out"
      }
    );
    
    this.animations.set(element, tl);
  }
  
  setFinalState(element) {
    // Instantly set final animation state for reduced motion users
    gsap.set(element, {
      opacity: 1,
      y: 0,
      x: 0,
      scale: 1,
      rotation: 0
    });
  }
}
```

### 2. Webflow Integration
```javascript
// Enhanced Webflow integration with conflict prevention
function initWebflowGSAP() {
  // Wait for Webflow to complete initialization
  function waitForWebflow(callback) {
    if (window.Webflow && document.readyState === 'complete') {
      callback();
    } else {
      setTimeout(() => waitForWebflow(callback), 100);
    }
  }
  
  waitForWebflow(() => {
    // Check for existing Webflow animations
    const webflowAnimations = document.querySelectorAll('[data-w-id]');
    if (webflowAnimations.length > 0) {
      console.log('Webflow animations detected, coordinating with GSAP');
    }
    
    // Initialize GSAP after Webflow is ready
    initUniversalGSAP();
  });
}
```

### 3. Focus Management for Animations
```javascript
// Accessibility-compliant focus management
function handleAnimationFocus(element, animation) {
  // Don't interrupt user focus
  if (document.activeElement === element || 
      element.contains(document.activeElement)) {
    return;
  }
  
  // Set up focus events
  element.addEventListener('focus', () => {
    if (animation.isActive()) {
      animation.pause();
    }
  });
  
  element.addEventListener('blur', () => {
    if (animation.paused()) {
      animation.resume();
    }
  });
}
```

## Latest GSAP Best Practices (2025)

### 1. Modern Timeline Management
```javascript
// Efficient timeline management
class GSAPTimelineManager {
  constructor() {
    this.timelines = new Map();
    this.globalTimeline = gsap.timeline();
  }
  
  create(id, options = {}) {
    const timeline = gsap.timeline({
      paused: true,
      ...options,
      onComplete: () => {
        this.cleanup(id);
        options.onComplete?.();
      }
    });
    
    this.timelines.set(id, timeline);
    return timeline;
  }
  
  play(id) {
    const timeline = this.timelines.get(id);
    if (timeline) {
      timeline.play();
    }
  }
  
  cleanup(id) {
    const timeline = this.timelines.get(id);
    if (timeline) {
      timeline.kill();
      this.timelines.delete(id);
    }
  }
  
  pauseAll() {
    this.timelines.forEach(timeline => timeline.pause());
  }
  
  resumeAll() {
    this.timelines.forEach(timeline => timeline.resume());
  }
}
```

### 2. Responsive Animation System
```javascript
// Responsive animations that adapt to screen size
function createResponsiveAnimations() {
  const breakpoints = {
    mobile: 768,
    tablet: 1024,
    desktop: 1440
  };
  
  function getDeviceType() {
    const width = window.innerWidth;
    if (width < breakpoints.mobile) return 'mobile';
    if (width < breakpoints.tablet) return 'tablet';
    if (width < breakpoints.desktop) return 'desktop';
    return 'large';
  }
  
  function getAnimationConfig(device) {
    const configs = {
      mobile: { duration: 0.4, distance: 20 },
      tablet: { duration: 0.5, distance: 30 },
      desktop: { duration: 0.6, distance: 40 },
      large: { duration: 0.7, distance: 50 }
    };
    
    return configs[device];
  }
  
  // Apply responsive animations
  const device = getDeviceType();
  const config = getAnimationConfig(device);
  
  return gsap.fromTo('.animate-element',
    { opacity: 0, y: config.distance },
    { 
      opacity: 1, 
      y: 0, 
      duration: config.duration,
      ease: "power2.out",
      stagger: 0.1
    }
  );
}
```

### 3. Performance Monitoring
```javascript
// Built-in performance monitoring for animations
function monitorGSAPPerformance() {
  let frameCount = 0;
  let startTime = performance.now();
  
  function trackFrame() {
    frameCount++;
    
    if (frameCount % 60 === 0) { // Check every 60 frames
      const currentTime = performance.now();
      const fps = 60000 / (currentTime - startTime);
      
      if (fps < 55) { // Below 55 FPS
        console.warn(`Animation performance: ${fps.toFixed(1)} FPS`);
      }
      
      startTime = currentTime;
    }
    
    requestAnimationFrame(trackFrame);
  }
  
  requestAnimationFrame(trackFrame);
}
```

## Dynamic GSAP Loading

### CDN with Fallback Strategy
```javascript
// Modern GSAP loading with fallback
async function loadGSAP() {
  const gsapSources = [
    'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js',
    'https://unpkg.com/gsap@3.12.5/dist/gsap.min.js'
  ];
  
  for (const src of gsapSources) {
    try {
      await loadScript(src);
      if (typeof gsap !== 'undefined') {
        console.log('GSAP loaded successfully');
        return true;
      }
    } catch (error) {
      console.warn(`Failed to load GSAP from ${src}`);
    }
  }
  
  console.error('All GSAP sources failed, using fallback');
  return false;
}

function loadScript(src) {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = src;
    script.onload = resolve;
    script.onerror = reject;
    document.head.appendChild(script);
  });
}
```

## Output Requirements

### Complete Animation System
1. **GSAP availability detection** with graceful fallbacks
2. **Accessibility compliance** with motion preference respect
3. **Performance monitoring** built-in
4. **Universal compatibility** (works beyond just Webflow)
5. **Error handling** for all failure scenarios

### Documentation Includes
- **Browser support matrix** with fallback strategies
- **Performance benchmarks** and optimization tips
- **Accessibility testing checklist**
- **Integration guides** for popular frameworks

## Cross-References
- Link to `smooth-scroll-2025` for scroll animation integration
- Reference `webflow-custom-js-optimizer` for performance optimization
- See `css-injection-pattern` for fallback animation styles

## Success Criteria
- **60fps performance** on all target devices
- **Zero accessibility violations** with automated testing
- **Graceful degradation** when GSAP unavailable
- **Sub-100ms initialization** time on modern browsers 