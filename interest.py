from math import log as ln

def present_amount( A0,p,n ):
    '''
    Calculate money after compounding A0 money for n days at p percent interest.
    '''
    return A0 * ( 1 + p / ( 360.0 * 100 ) ) ** n

def initial_amount( A,p,n ):
    return A * ( 1 + p / ( 360.0 * 100 ) ) ** -n

def days( A0,A,p ):
    return ln( A/A0 ) / ln( 1 + p / ( 360.0 * 100 ) )

def annual_rate( A0,A,n ):
    return 360 * 100 * ( ( A / A0 ) ** ( 1 / n ) - 1 )