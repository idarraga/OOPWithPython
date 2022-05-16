#include <stdlib.h>
#include <math.h>

#define GRAV_CNST 4.904099987329075e-10

void calc_force(double x1, double x2, double v1, double v2, double m1, double m2, double *array_out)
{
    double dx = x1-x2;
    double dy = v1-v2;
    double dist = sqrt(dx*dx + dy*dy);
    
    array_out[0] = -1.0 * (dx/dist) * GRAV_CNST * m1*m2 / (dist * dist);
    array_out[1] = -1.0 * (dy/dist) * GRAV_CNST * m1*m2 / (dist * dist);
}
