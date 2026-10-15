import os

html_test = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Logo Geometry Visual Exploration</title>
  <style>
    body {
      background: #090D16;
      color: #F8FAFC;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0;
      padding: 40px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 40px;
    }
    h1 { font-weight: 300; letter-spacing: 4px; text-transform: uppercase; margin: 0; font-size: 24px; color: #94A3B8; }
    .grid {
      display: grid;
      grid-template-columns: repeat(2, 480px);
      gap: 30px;
    }
    .card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      padding: 30px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }
    .card-title {
      font-size: 14px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #38BDF8;
      font-weight: 600;
    }
    .logo-box {
      width: 280px;
      height: 280px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .light-card {
      background: #FFFFFF;
      color: #09090B;
    }
    .light-card .card-title {
      color: #0284C7;
    }
    svg {
      width: 100%;
      height: 100%;
    }
  </style>
</head>
<body>
  <h1>AURA &bull; Logo Design Exploration</h1>
  
  <div class="grid">
    <!-- Option A: Continuous Möbius Loop -->
    <div class="card">
      <div class="card-title">Concept A &bull; Continuous Möbius Ribbon</div>
      <div class="logo-box">
        <svg viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="mobiusGrad1" x1="120" y1="400" x2="250" y2="80" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stop-color="#00F2FE"/>
              <stop offset="100%" stop-color="#4FACFE"/>
            </linearGradient>
            <linearGradient id="mobiusGrad2" x1="250" y1="80" x2="380" y2="400" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stop-color="#4FACFE"/>
              <stop offset="60%" stop-color="#6366F1"/>
              <stop offset="100%" stop-color="#8B5CF6"/>
            </linearGradient>
            <linearGradient id="mobiusGrad3" x1="150" y1="300" x2="350" y2="300" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stop-color="#A855F7"/>
              <stop offset="100%" stop-color="#00F2FE"/>
            </linearGradient>
          </defs>
          
          <!-- Outer Apex Ribbon -->
          <path d="M 120 390 L 250 110 L 380 390" stroke="url(#mobiusGrad2)" stroke-width="48" stroke-linecap="round" stroke-linejoin="round"/>
          <!-- Inner Mobius Crossbar & Loop -->
          <path d="M 180 300 Q 250 250 320 300 Q 370 340 320 380 Q 250 420 180 360" stroke="url(#mobiusGrad1)" stroke-width="44" stroke-linecap="round" fill="none"/>
        </svg>
      </div>
    </div>

    <!-- Option B: Isometric Prismatic Apex (Geometric Precision) -->
    <div class="card">
      <div class="card-title">Concept B &bull; Prismatic Precision Apex</div>
      <div class="logo-box">
        <svg viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="prismGrad1" x1="100" y1="420" x2="250" y2="90" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stop-color="#00F2FE"/>
              <stop offset="60%" stop-color="#38BDF8"/>
              <stop offset="100%" stop-color="#4F46E5"/>
            </linearGradient>
            <linearGradient id="prismGrad2" x1="250" y1="90" x2="400" y2="420" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stop-color="#4F46E5"/>
              <stop offset="50%" stop-color="#7C3AED"/>
              <stop offset="100%" stop-color="#9333EA"/>
            </linearGradient>
            <linearGradient id="prismGrad3" x1="130" y1="350" x2="370" y2="350" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stop-color="#38BDF8"/>
              <stop offset="50%" stop-color="#6366F1"/>
              <stop offset="100%" stop-color="#C084FC"/>
            </linearGradient>
          </defs>
          
          <!-- Facet Left Ascent -->
          <path d="M 250 85 L 210 90 L 105 385 L 165 385 L 235 190 L 250 150 Z" fill="url(#prismGrad1)"/>
          <!-- Facet Right Descent -->
          <path d="M 250 85 L 290 90 L 395 385 L 335 385 L 265 190 L 250 150 Z" fill="url(#prismGrad2)"/>
          <!-- Interlocking Horizon Möbius Crossbar -->
          <path d="M 150 325 L 350 325 L 315 260 L 185 260 Z" fill="url(#prismGrad3)" opacity="0.95"/>
          <!-- Inner Aperture Cutout -->
          <polygon points="250,175 195,315 305,315" fill="#090D16" />
        </svg>
      </div>
    </div>

    <!-- Option C: Pure Minimalist Monogram (KISS Principle) -->
    <div class="card">
      <div class="card-title">Concept C &bull; Pure Minimalist Ribbon (KISS)</div>
      <div class="logo-box">
        <svg viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="kissGrad" x1="0%" y1="100%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#06B6D4"/>
              <stop offset="50%" stop-color="#3B82F6"/>
              <stop offset="100%" stop-color="#8B5CF6"/>
            </linearGradient>
          </defs>
          <!-- Outer architectural arch with continuous inner counter-loop -->
          <!-- A single uninterrupted continuous stroke forming an 'A' -->
          <path d="M 120 400 L 250 100 L 380 400 L 310 400 L 250 255 L 190 400 Z" fill="url(#kissGrad)"/>
          <!-- Floating ambient core horizon -->
          <rect x="180" y="320" width="140" height="28" rx="14" fill="#38BDF8"/>
        </svg>
      </div>
    </div>

    <!-- Option D: The Penrose Möbius (As in Mockup) -->
    <div class="card">
      <div class="card-title">Concept D &bull; Dimensional Möbius Penrose</div>
      <div class="logo-box">
        <svg viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="penGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#38BDF8"/>
              <stop offset="100%" stop-color="#2563EB"/>
            </linearGradient>
            <linearGradient id="penGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#4F46E5"/>
              <stop offset="100%" stop-color="#7C3AED"/>
            </linearGradient>
            <linearGradient id="penGrad3" x1="0%" y1="100%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#0284C7"/>
              <stop offset="100%" stop-color="#6366F1"/>
            </linearGradient>
          </defs>
          <!-- Facet A: Top-Left to Bottom-Left -->
          <polygon points="250,80 290,148 185,330 115,330 215,150" fill="url(#penGrad1)"/>
          <!-- Facet B: Top to Bottom-Right -->
          <polygon points="250,80 385,330 315,330 250,210 215,150" fill="url(#penGrad2)"/>
          <!-- Facet C: Bottom Cross-Ribbon -->
          <polygon points="115,330 385,330 345,395 155,395" fill="url(#penGrad3)"/>
          <!-- Inner Core Triangle -->
          <polygon points="250,210 290,285 210,285" fill="#06B6D4" opacity="0.9"/>
        </svg>
      </div>
    </div>
  </div>
</body>
</html>
"""

with open("showcase/explore.html", "w", encoding="utf-8") as f:
    f.write(html_test)

print("Exploration page created at showcase/explore.html")
