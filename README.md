## Intro
- Capture your face and preserve daily records, then display the changes in a long period of time
- Pipeline: Detect face bounding box --> Face landmark detection --> Align and crop face w.r.t the landmarks --> save daily face image --> generate .gif displaying these records.
## Usage
- run script ```python run.py``` for daily record  
- press <Enter> to capture a face
- press <Enter> again to confirm. if not, back to the previous step
- run script ```python process.py``` to generate .gif file
