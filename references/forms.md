# Forms — ND Web Theme v4

Form markup patterns from the official NDT4 Storybook.

**Contents:** Form layouts, Individual controls

## Form layouts

Complete form patterns. Note: Conductor pages can't run custom server-side handlers — forms usually point at Qualtrics, Formstack, Google Forms, or a service endpoint; often it's better to *link out* to the form. Use these patterns when embedding a search/filter UI or building markup for an external handler.

**Basic Search Form**

```html
<div class="form-combinations"><h2 class="form-title">Search</h2><div class="form-field">
    <label for="input-x5m7v0dh">Search</label>
    <input class="field" id="input-x5m7v0dh" type="search" placeholder="Search Site Name">
    
  </div><button class="btn btn-primary mt-4" type="submit">Search</button></div>
```

**Contact Form**

```html
<div class="form-combinations"><h2 class="form-title">Contact Information</h2><div class="form-field">
    <label for="input-wzd403vm">First Name</label>
    <input class="field" id="input-wzd403vm" type="text" placeholder="Enter your first name">
    
  </div><div class="form-field">
    <label for="input-1qzus14m">Last Name</label>
    <input class="field" id="input-1qzus14m" type="text" placeholder="Enter your last name">
    
  </div><div class="form-field">
    <label for="input-ebecvis5">Email</label>
    <input class="field" id="input-ebecvis5" type="email" placeholder="email@nd.edu">
    
  </div><div class="form-field">
    <label for="input-iifnj2cy">Phone</label>
    <input class="field" id="input-iifnj2cy" type="text" placeholder="(574) 631-5000">
    
  </div><div class="form-field">
    <label for="select-erjmvwud">Department</label>
    <select class="field" name="select-erjmvwud" id="select-erjmvwud">
    <option value="admissions">Admissions</option>
      <option value="registrar">Registrar</option>
      <option value="financialaid">Financial Aid</option>
      <option value="studentaffairs">Student Affairs</option>
    </select>
    
  </div><div class="form-field">
    <label for="textarea-o1n9zozj">Message</label>
    <textarea id="textarea-o1n9zozj" rows="4" placeholder="Your message here..."></textarea>
      
  </div><div class="form-field">
    <label for="checkbox-bm9o3w22">Interests</label>
    <ul class="no-bullets field checkbox-list">
    <li><input id="checkbox-0" type="checkbox" name="checkbox-group"><label for="checkbox-0">Campus Tours</label></li>
      <li><input id="checkbox-1" type="checkbox" name="checkbox-group"><label for="checkbox-1">Information Sessions</label></li>
      <li><input id="checkbox-2" type="checkbox" name="checkbox-group"><label for="checkbox-2">Alumni Events</label></li>
    </ul>
    
  </div><div class="form-field">
    <label for="radio-kg8lgobe">Preferred Contact Method</label>
    <ul class="field no-bullets radio-list" id="radio-kg8lgobe">
      <li><input id="radio-0" type="radio" name="radio-group"><label for="radio-0">Email</label></li>
        <li><input id="radio-1" type="radio" name="radio-group"><label for="radio-1">Phone</label></li>
    </ul>
    
  </div><button class="btn btn-primary mt-4" type="submit">Send Message</button></div>
```


## Individual controls

**Default Input**

```html
<div class="form-field">
    
    <input class="field" id="input-1knyxhbz" type="text" placeholder="">
    
  </div>
```

**With Label**

```html
<div class="form-field">
    <label for="select-x4nnqc3x">Choose an option</label>
    <select class="field" name="select-x4nnqc3x" id="select-x4nnqc3x">
    <option value="option1">Option 1</option>
      <option value="option2">Option 2</option>
      <option value="option3">Option 3</option>
    </select>
    
  </div>
```

**Default Checkbox Group**

```html
<div class="form-field">
    
    <ul class="no-bullets field checkbox-list">
    <li><input id="checkbox-0" type="checkbox" name="checkbox-group"><label for="checkbox-0">Checkbox Input 1 (Default)</label></li>
      <li><input id="checkbox-1" type="checkbox" disabled="" name="checkbox-group"><label for="checkbox-1">Checkbox Input 2 (Disabled)</label></li>
      <li><input id="checkbox-2" type="checkbox" checked="" name="checkbox-group"><label for="checkbox-2">Checkbox Input 3 (Checked)</label></li>
    </ul>
    
  </div>
```

**Default Radio Group**

```html
<div class="form-field">
    
    <ul class="field no-bullets radio-list" id="radio-nuf2x8ym">
      <li><input id="radio-0" type="radio" name="radio-group"><label for="radio-0">Radio Input 1</label></li>
        <li><input id="radio-1" type="radio" checked="" name="radio-group"><label for="radio-1">Radio Input 2 (Selected)</label></li>
        <li><input id="radio-2" type="radio" disabled="" name="radio-group"><label for="radio-2">Radio Input 3 (Disabled)</label></li>
    </ul>
    
  </div>
```

**With Note**

```html
<div class="form-field">
    
    <textarea id="help-text-textarea" rows="3" placeholder="Enter text here..."></textarea>
    <p class="form-field-note">This is some help text.</p>  
  </div>
```

**With Label**

```html
<div class="form-field">
    <span class="label">Toggle Me</span>
    <label class="switch field">
      <input type="checkbox">
      <span class="slider"></span>
    </label>
    
  </div>
```

