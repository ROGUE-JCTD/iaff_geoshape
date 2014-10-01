<?xml version="1.0" encoding="ISO-8859-1"?>
<StyledLayerDescriptor version="1.0.0"
 xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd"
 xmlns="http://www.opengis.net/sld"
 xmlns:ogc="http://www.opengis.net/ogc"
 xmlns:xlink="http://www.w3.org/1999/xlink"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <!-- a Named Layer is the basic building block of an SLD document -->
  <NamedLayer>
    <Name>Hydrants</Name>
    <UserStyle>
    <!-- Styles can have names, titles and abstracts -->
      <Title>Hydrants</Title>
      <Abstract>A sample style that draws a point</Abstract>
      <!-- FeatureTypeStyles describe how to render different features -->
      <!-- A FeatureTypeStyle for rendering points -->
      <FeatureTypeStyle>
        <Rule>
          <Name>Blue Hydrants</Name>
          <Title>Blue Hydrant</Title>
          <Abstract>A 6 pixel circle with a blue fill and no stroke.</Abstract>
          <Filter xmlns="http://www.opengis.net/ogc">
            <PropertyIsEqualTo>
              <PropertyName>fd_color</PropertyName>
              <Literal>Blue</Literal>
            </PropertyIsEqualTo>
          </Filter>
            <PointSymbolizer>
              <Graphic>
                <Mark>
                  <WellKnownName>circle</WellKnownName>
                  <Fill>
                    <CssParameter name="fill">#0074D9</CssParameter>
                  </Fill>
                </Mark>
              <Size>6</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
        <Rule>
          <Name>Orange Hydrants</Name>
          <Title>Orange Hydrant</Title>
          <Abstract>A 6 pixel circle with an orange fill and no stroke.</Abstract>
          <Filter xmlns="http://www.opengis.net/ogc">
            <PropertyIsEqualTo>
              <PropertyName>fd_color</PropertyName>
              <Literal>Orange</Literal>
            </PropertyIsEqualTo>
          </Filter>
            <PointSymbolizer>
              <Graphic>
                <Mark>
                  <WellKnownName>circle</WellKnownName>
                  <Fill>
                    <CssParameter name="fill">#FF851B</CssParameter>
                  </Fill>
                </Mark>
              <Size>6</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
        <Rule>
          <Name>Green Hydrants</Name>
          <Title>Green Hydrant</Title>
          <Abstract>A 6 pixel circle with a green fill and no stroke.</Abstract>
          <Filter xmlns="http://www.opengis.net/ogc">
            <PropertyIsEqualTo>
              <PropertyName>fd_color</PropertyName>
              <Literal>Green</Literal>
            </PropertyIsEqualTo>
          </Filter>
            <PointSymbolizer>
              <Graphic>
                <Mark>
                  <WellKnownName>circle</WellKnownName>
                  <Fill>
                    <CssParameter name="fill">#2ECC40</CssParameter>
                  </Fill>
                </Mark>
              <Size>6</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
        <Rule>
          <Name>Red Hydrants</Name>
          <Title>Red Hydrant</Title>
          <Abstract>A 6 pixel circle with a red fill and no stroke.</Abstract>
          <Filter xmlns="http://www.opengis.net/ogc">
            <PropertyIsEqualTo>
              <PropertyName>fd_color</PropertyName>
              <Literal>Red</Literal>
            </PropertyIsEqualTo>
          </Filter>
            <PointSymbolizer>
              <Graphic>
                <Mark>
                  <WellKnownName>circle</WellKnownName>
                  <Fill>
                    <CssParameter name="fill">#FF4136</CssParameter>
                  </Fill>
                </Mark>
              <Size>6</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
        <Rule>
          <Name>Other Hydrants</Name>
          <Title>Other Hydrant</Title>
          <Abstract>A 6 pixel circle with a black fill and no stroke.</Abstract>
          <Filter xmlns="http://www.opengis.net/ogc">
            <And>
              <PropertyIsNotEqualTo>
                <PropertyName>fd_color</PropertyName>
                <Literal>Red</Literal>
              </PropertyIsNotEqualTo>
              <PropertyIsNotEqualTo>
                <PropertyName>fd_color</PropertyName>
                <Literal>Orange</Literal>
              </PropertyIsNotEqualTo>
              <PropertyIsNotEqualTo>
                <PropertyName>fd_color</PropertyName>
                <Literal>Green</Literal>
              </PropertyIsNotEqualTo>
              <PropertyIsNotEqualTo>
                <PropertyName>fd_color</PropertyName>
                <Literal>Blue</Literal>
              </PropertyIsNotEqualTo>
            </And>
          </Filter>
            <PointSymbolizer>
              <Graphic>
                <Mark>
                  <WellKnownName>circle</WellKnownName>
                  <Fill>
                    <CssParameter name="fill">#111111</CssParameter>
                  </Fill>
                </Mark>
              <Size>6</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
