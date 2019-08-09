import { Component, OnInit } from '@angular/core';
import { flushMicrotasks } from '@angular/core/testing';
import { AppService } from '../app.service';

@Component({
  selector: 'app-faculty',
  templateUrl: './faculty.component.html',
  styleUrls: ['./faculty.component.css']
})


export class FacultyComponent implements OnInit {
 
  constructor(private appService:AppService) {

  }

  ngOnInit() {
    
  }
