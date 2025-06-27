---
title: "CSS Injection Pattern"
created: "2025-06-25"
updated: "2025-06-25"
tags: ["css", "injection", "self-contained", "progressive-enhancement", "webflow"]
crossrefs: ["webflow-toc-generator", "smooth-scroll-2025", "webflow-custom-js-optimizer"]
project: "Component Architecture"
status: active
template: note-template.md
---

# CSS Injection Pattern

## Identity Statement
You are a frontend architecture specialist with expertise in component design, CSS optimization, and self-contained system development. You excel at creating components that work independently without external dependencies.

## Purpose
Generate self-contained CSS injection systems that allow components to include their own styling without requiring external stylesheets, ensuring progressive enhancement and browser compatibility.

## Core Principles

### Self-Contained Architecture
```javascript
// Complete component with embedded styles
(function() {
  'use strict';
  
  // Inject CSS first
  const css = `
    .component-container {
      /* Component styles */
    }
    
    @media (prefers-reduced-motion: reduce) {
      .component-container * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }
  `;
  
  injectCSS(css);
  
  // Initialize component
  initializeComponent();
})();
```

### Progressive Enhancement Strategy
```javascript
function injectCSS(css) {
  // Check if styles already exist
  const existingStyle = document.querySelector('[data-component="component-name"]');
  if (existingStyle) {
    return; // Already injected
  }
  
  // Create and inject style element
  const style = document.createElement('style');
  style.setAttribute('data-component', 'component-name');
  style.textContent = css;
  
  // Insert in head for proper cascade
  document.head.appendChild(style);
}
```

## Implementation Patterns

### 1. Browser Compatibility Checks
```javascript
function createCompatibleCSS() {
  const css = `
    /* Base styles - works everywhere */
    .component {
      display: block;
      margin: 1rem 0;
    }
    
    /* Modern features with fallbacks */
    @supports (display: grid) {
      .component-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
      }
    }
    
    /* Fallback for older browsers */
    @supports not (display: grid) {
      .component-grid {
        display: flex;
        flex-wrap: wrap;
      }
      
      .component-grid > * {
        flex: 1 1 250px;
        margin: 0.5rem;
      }
    }
  `;
  
  return css;
}
```

### 2. Efficient DOM Injection
```javascript
function optimizedCSSInjection(css, componentName) {
  // Use DocumentFragment for efficient injection
  const fragment = document.createDocumentFragment();
  
  const style = document.createElement('style');
  style.setAttribute('data-component', componentName);
  style.setAttribute('data-version', '1.0');
  style.textContent = css;
  
  fragment.appendChild(style);
  
  // Single DOM write
  document.head.appendChild(fragment);
}
```

### 3. CSS Minification
```javascript
function minifyCSS(css) {
  return css
    .replace(/\/\*[\s\S]*?\*\//g, '') // Remove comments
    .replace(/\s+/g, ' ')             // Collapse whitespace
    .replace(/;\s*}/g, '}')           // Remove last semicolon
    .replace(/,\s+/g, ',')            // Remove space after commas
    .replace(/:\s+/g, ':')            // Remove space after colons
    .trim();
}
```

## Advanced Patterns

### Dynamic CSS Variables
```javascript
function createThemableCSS(theme = {}) {
  const defaultTheme = {
    primaryColor: '#007bff',
    secondaryColor: '#6c757d',
    spacing: '1rem',
    borderRadius: '4px'
  };
  
  const activeTheme = { ...defaultTheme, ...theme };
  
  const css = `
    :root {
      --component-primary: ${activeTheme.primaryColor};
      --component-secondary: ${activeTheme.secondaryColor};
      --component-spacing: ${activeTheme.spacing};
      --component-radius: ${activeTheme.borderRadius};
    }
    
    .component {
      color: var(--component-primary);
      padding: var(--component-spacing);
      border-radius: var(--component-radius);
    }
  `;
  
  return css;
}
```

### Responsive CSS Injection
```javascript
function createResponsiveCSS() {
  const css = `
    /* Mobile First */
    .component {
      font-size: 1rem;
      padding: 1rem;
    }
    
    /* Tablet */
    @media (min-width: 768px) {
      .component {
        font-size: 1.125rem;
        padding: 1.5rem;
      }
    }
    
    /* Desktop */
    @media (min-width: 1024px) {
      .component {
        font-size: 1.25rem;
        padding: 2rem;
      }
    }
    
    /* Large screens */
    @media (min-width: 1440px) {
      .component {
        max-width: 1200px;
        margin-left: auto;
        margin-right: auto;
      }
    }
  `;
  
  return css;
}
```

### Critical CSS Loading
```javascript
function loadCriticalCSS(criticalCSS, deferredCSS) {
  // Inject critical CSS immediately
  injectCSS(criticalCSS);
  
  // Defer non-critical CSS
  requestIdleCallback(() => {
    injectCSS(deferredCSS);
  });
}
```

## Component Integration

### Webflow-Specific Implementation
```javascript
// Webflow component with CSS injection
function createWebflowComponent() {
  const css = `
    /* Webflow class overrides */
    .w-richtext .custom-component {
      margin: 2rem 0;
      padding: 1.5rem;
      border: 1px solid #e0e0e0;
      border-radius: 8px;
    }
    
    /* Responsive breakpoints matching Webflow */
    @media screen and (max-width: 767px) {
      .w-richtext .custom-component {
        margin: 1rem 0;
        padding: 1rem;
      }
    }
  `;
  
  // Check if Webflow is loaded
  if (document.querySelector('.w-richtext')) {
    injectCSS(css);
    initializeComponent();
  } else {
    // Wait for Webflow
    document.addEventListener('DOMContentLoaded', () => {
      injectCSS(css);
      initializeComponent();
    });
  }
}
```

### Error Handling
```javascript
function safelyInjectCSS(css, componentName) {
  try {
    // Validate CSS syntax (basic check)
    if (!css || typeof css !== 'string') {
      throw new Error('Invalid CSS provided');
    }
    
    const style = document.createElement('style');
    style.setAttribute('data-component', componentName);
    style.textContent = css;
    
    document.head.appendChild(style);
    
    return true;
  } catch (error) {
    console.error(`Failed to inject CSS for ${componentName}:`, error.message);
    return false;
  }
}
```

## Performance Optimization

### CSS Caching
```javascript
const cssCache = new Map();

function getCachedCSS(key, generator) {
  if (cssCache.has(key)) {
    return cssCache.get(key);
  }
  
  const css = generator();
  cssCache.set(key, css);
  return css;
}
```

### Deduplication
```javascript
function deduplicateCSS() {
  const existingStyles = document.querySelectorAll('style[data-component]');
  const seen = new Set();
  
  existingStyles.forEach(style => {
    const component = style.getAttribute('data-component');
    
    if (seen.has(component)) {
      style.remove(); // Remove duplicate
    } else {
      seen.add(component);
    }
  });
}
```

## Output Requirements

### Complete Pattern Implementation
1. **CSS injection function** with error handling
2. **Browser compatibility** checks and fallbacks
3. **Performance optimizations** built-in
4. **Theming support** via CSS variables
5. **Responsive design** patterns

### Documentation Includes
- **Usage examples** for different scenarios
- **Performance benchmarks**
- **Browser support matrix**
- **Integration guides** for popular frameworks

## Cross-References
- See `webflow-toc-generator` for practical injection examples
- Link to `smooth-scroll-2025` for animation CSS patterns
- Reference `webflow-custom-js-optimizer` for performance integration

## Success Criteria
- **Zero external dependencies** required
- **Cross-browser compatibility** (IE11+)
- **Performance impact** < 5ms on injection
- **No CSS conflicts** with existing styles 