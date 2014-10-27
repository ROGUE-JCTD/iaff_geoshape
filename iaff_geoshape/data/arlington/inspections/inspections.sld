<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor version="1.0.0"
  xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd"
  xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
  xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <NamedLayer>
    <Name>arlington_inspections</Name>
    <UserStyle>
      <FeatureTypeStyle>
          <Rule>
          <Title>(N) Permit-No Violations</Title>
            <Filter xmlns="http://www.opengis.net/ogc">
              <PropertyIsEqualTo>
                <PropertyName>inspection_type</PropertyName>
                <Literal>(N) Permit-No Violations</Literal>
              </PropertyIsEqualTo>
            </Filter>
             <PointSymbolizer>
               <Graphic>
               <Mark>
                 <WellKnownName>triangle</WellKnownName>
                 <Fill>
                   <CssParameter name="fill">#2ECC40</CssParameter>
                 </Fill>
               </Mark>
               <Size>10</Size>
               </Graphic>
             </PointSymbolizer>
        </Rule>
        <Rule>
          <Title>Permit violations</Title>
            <Filter xmlns="http://www.opengis.net/ogc">
              <PropertyIsEqualTo>
                <PropertyName>inspection_type</PropertyName>
                <Literal>Permit violations</Literal>
              </PropertyIsEqualTo>
            </Filter>
             <PointSymbolizer>
               <Graphic>
               <Mark>
                 <WellKnownName>triangle</WellKnownName>
                 <Fill>
                   <CssParameter name="fill">#FF4136</CssParameter>
                 </Fill>
               </Mark>
               <Size>10</Size>
               </Graphic>
             </PointSymbolizer>
        </Rule>
        <Rule>
          <Title>(N) Annual-No Violations</Title>
            <Filter xmlns="http://www.opengis.net/ogc">
              <PropertyIsEqualTo>
                <PropertyName>inspection_type</PropertyName>
                <Literal>(N) Annual-No Violations</Literal>
              </PropertyIsEqualTo>
            </Filter>
             <PointSymbolizer>
               <Graphic>
               <Mark>
                 <WellKnownName>triangle</WellKnownName>
                 <Fill>
                   <CssParameter name="fill">#3D9970</CssParameter>
                 </Fill>
               </Mark>
               <Size>10</Size>
               </Graphic>
             </PointSymbolizer>
        </Rule>
       <Rule>
          <Title>Annual-Violations</Title>
            <Filter xmlns="http://www.opengis.net/ogc">
              <PropertyIsEqualTo>
                <PropertyName>inspection_type</PropertyName>
                <Literal>Annual-Violations</Literal>
              </PropertyIsEqualTo>
            </Filter>
             <PointSymbolizer>
               <Graphic>
               <Mark>
                 <WellKnownName>triangle</WellKnownName>
                 <Fill>
                   <CssParameter name="fill">#FF851B</CssParameter>
                 </Fill>
               </Mark>
               <Size>10</Size>
               </Graphic>
             </PointSymbolizer>
        </Rule>
       <Rule>
          <Title>Hoarding</Title>
            <Filter xmlns="http://www.opengis.net/ogc">
              <PropertyIsEqualTo>
                <PropertyName>inspection_type</PropertyName>
                <Literal>Hoarding</Literal>
              </PropertyIsEqualTo>
            </Filter>
             <PointSymbolizer>
               <Graphic>
               <Mark>
                 <WellKnownName>triangle</WellKnownName>
                 <Fill>
                   <CssParameter name="fill">#111111</CssParameter>
                 </Fill>
               </Mark>
               <Size>10</Size>
               </Graphic>
             </PointSymbolizer>
        </Rule>  
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>

