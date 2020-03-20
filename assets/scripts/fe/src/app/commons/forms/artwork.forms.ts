import {
  FormBuilder,
  FormGroup,
  FormControl,
  Validators
} from '@angular/forms';


export class ArtWorkForm {
  public artworkForm: FormGroup;
  public errors: string = null;

  constructor(data) {
      // Initialize the form builder
      this.artworkForm = new FormBuilder().group({
          featured_image: new FormControl(null, [Validators.required]),
          title: new FormControl(null, [Validators.required]),
          description: new FormControl(null),
          image: new FormControl(null),
          is_free: new FormControl(true),
          price: new FormControl({value: null, disabled: true})
      });
  }

  // check if form field is valid
  valid(f: any) {
      return !(!this.artworkForm.get(f).valid && this.artworkForm.get(f).touched);
  }

  // check if the form field has an error
  hasError(f: any, e: any) {
      return this.artworkForm.get(f).hasError(e) && this.artworkForm.get(f).touched;
  }
}
