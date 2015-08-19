/* Derived by Carlosgs from:
 * http://www.thingiverse.com/thing:12789
 * An extruder gear set for the TechZone Huxley,
 *  featuring Herringbone teeth.
 * You will have to recalibrate your E_STEPS_PER_MM in
 *  your firmware (ratio changing from original techzone
 *  lasercut gears).
 * This use 2 modules from the MCAD library that you can
 *  get from https://github.com/elmom/MCAD.
 * 
 * Part - the motor gear mount hub with set screw hole -
 *  derived from http://www.thingiverse.com/thing:3104
 *  (thanks GilesBathgate) which is under GPL CC license.
 *
 * Copyright (C) 2011  Guy 'DeuxVis' P.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.

 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 * -- 
 *     DeuxVis - device@ymail.com */

include <MCAD/metric_fastners.scad>
include <MCAD/materials.scad>
include <MCAD/teardrop.scad>
include <MCAD/involute_gears.scad>


M8_nut_diameter = 15.3;
nut_separation = 3;

SmallGear_N_Teeth = 15; // 12
M8_rod_diam = 8.6;

/* Herringbone gear module, adapted from MCAD/involute_gears */
module herringbone_gear( teeth=12, circles=0, shaft=5 ) {
  twist=200;
  height=10;
  pressure_angle=30;

  gear(
    number_of_teeth=teeth,
    circular_pitch=320,
		pressure_angle=pressure_angle,
		clearance = 0.2,
		gear_thickness = height/2,
		rim_thickness = height/2,
		rim_width = 1,
		hub_thickness = height/2,
		hub_diameter=1,
		bore_diameter=shaft,
		circles=circles,
		twist=twist/teeth
  );

	mirror( [0,0,1] )
	  gear(
      number_of_teeth=teeth,
		  circular_pitch=320,
		  pressure_angle=pressure_angle,
		  clearance = 0.2,
		  gear_thickness = height/2,
		  rim_thickness = height/2,
		  rim_width = 1,
		  hub_thickness = height/2,
		  hub_diameter=1,
		  bore_diameter=shaft,
		  circles=circles,
		  twist=twist/teeth
    );
	translate([0,0,-5])
		rotate([0,0,-13.5])
			mirror( [0,0,1] )
			  gear(
		      number_of_teeth=teeth,
				  circular_pitch=320,
				  pressure_angle=30,
				  clearance = 0.2,
				  gear_thickness = 3,//height/2,
				  rim_thickness = 3,//height/2,
				  rim_width = 1,
				  hub_thickness = 3,//height/2,
				  hub_diameter=1,
				  bore_diameter=shaft,
				  circles=circles,
				  twist=120/teeth
		    );
}

module rod_gear(with_extra_parts=false, exploded=false) {
// Extruder Gear
difference() {
  union() {
    //gear
    rotate([180,0,0]) herringbone_gear( teeth=SmallGear_N_Teeth, circles=0, shaft=M8_rod_diam, $fn=40 );

    //M8 hobbed bolt head fit washer
    /*difference() {
      translate( [0, 0, 5] ) cylinder( r=8, h=3, $fn=60 );
      translate( [0, 0, 5-0.01] ) cylinder( r=M8_nut_diameter/2, h=7, $fn=6 );
    }*/
    /*rotate([180,0,0]) difference() {
      translate( [0, 0, 5] ) cylinder( r=13, h=3, $fn=60 );
      translate( [0, 0, 5+0.4] ) cylinder( r=M8_nut_diameter/2, h=7, $fn=6 );
    }*/
  }

  //translate( [0, 0, (nut_separation/2)] ) cylinder( r=M8_nut_diameter/2, h=7, $fn=6 );
}

  if(with_extra_parts)
    cyclone_rod_gear_extras(exploded_distance=(exploded?12:0));

  module cyclone_rod_gear_extras(exploded_distance=0) {
    echo("Non-Plastic Parts, 2, Nut M8 to attach rod_gear on threaded rod");
    translate([0,0,-10/2-0.8*8-1.0*exploded_distance]) color(Steel) flat_nut(8);
    translate([0,0,nut_separation/2+0.8*8+1.0*exploded_distance]) rotate([180,0,0]) color(Steel) flat_nut(8);
  }

}


M8_nut_diameter = 15.3;
nut_separation = 1;

motor_shaft_diameter=8.6;
BigGear_N_Teeth = 21; // 24

nholes = 9; // 7
holes_diam = 6;
hole_distance_from_center = 13.5-4.5+holes_diam/2;

/* Herringbone gear module, adapted from MCAD/involute_gears */
module herringbone_gear_b( teeth=12, circles=0, shaft=5 ) {
  twist=200;
  height=10;
  pressure_angle=30;

  gear(
    number_of_teeth=teeth,
    circular_pitch=320,
		pressure_angle=pressure_angle,
		clearance = 0.2,
		gear_thickness = height/2,
		rim_thickness = height/2,
		rim_width = 1,
		hub_thickness = height/2,
		hub_diameter=1,
		bore_diameter=shaft,
		circles=circles,
		twist=twist/teeth
  );

	mirror( [0,0,1] )
	  gear(
      number_of_teeth=teeth,
		  circular_pitch=320,
		  pressure_angle=pressure_angle,
		  clearance = 0.2,
		  gear_thickness = height/2,
		  rim_thickness = height/2,
		  rim_width = 1,
		  hub_thickness = height/2,
		  hub_diameter=1,
		  bore_diameter=shaft,
		  circles=circles,
		  twist=twist/teeth
    );
}

module rod_gear_big() {
// Motor gear
union() difference() {	 
  union() {
    //gear
    herringbone_gear_b( teeth=BigGear_N_Teeth );	
  }
	translate( [0, 0, (nut_separation/2)] ) cylinder( r=M8_nut_diameter/2, h=7, $fn=6 );


  //shaft hole
  translate( [0, 0, -6] ) cylinder( r=motor_shaft_diameter/2, h=20, $fn=30 );
}

}

//rod_gear_big();

rod_gear();
translate([0,0,13]) rod_gear_big();
