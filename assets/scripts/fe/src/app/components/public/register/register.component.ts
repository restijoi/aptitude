import { Component, OnInit } from '@angular/core';
import { StateService } from '@uirouter/angular';

import { AuthService } from '../../../commons/services/auth/auth.service';
import { Register } from '../../../commons/models/register.models';
import { RegisterForm } from '../../../commons/forms/register.forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  public form: RegisterForm;

  constructor(
    private auth: AuthService,
    private state: StateService
  ) { }

  ngOnInit(): void {
    this.form = new RegisterForm(new Register());
  }

  onSubmit({value, valid}: {value: Register, valid: boolean}) {
    if (valid) {
      // send the data to the backend server
      this.auth.register(value)
        .then((resp: any) => {
          console.log( resp )
          // redirect to the dashboard
          if (resp) {
            this.state.go('home');
          }
        })
        .catch((err: any) => {
          this.form.errors = err;
        })
      ;
    }
  }

}
