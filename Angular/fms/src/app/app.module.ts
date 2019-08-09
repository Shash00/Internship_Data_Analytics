import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule} from '@angular/forms'
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FacultyComponent } from './faculty/faculty.component';
import { HeaderComponent } from './header/header.component';
import { LabComponent } from './lab/lab.component';
import { WhoursComponent } from './whours/whours.component';
import { AppService } from './app.service';



@NgModule({
  declarations: [
    AppComponent,
    FacultyComponent,
    HeaderComponent,
    LabComponent,
    WhoursComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [AppService],
  bootstrap: [AppComponent]
})
export class AppModule { }
