import React, { useState, useCallback, useMemo, useRef } from "react";
import { Col, Container, Form, Row } from "react-bootstrap";

interface WebSocketDemoInterface {
  messages: string[];
}
export const WebSocketDemo = (props: WebSocketDemoInterface) => {
  const { messages } = props;
  React.useEffect(() => {});
  console.log("stanley", messages);
  return (
    <Container>
      <Row>
        <Col xs={6}>
          <Form className="col-xs-12">
            <Form.Group controlId="exampleForm.ControlTextarea1">
              <Form.Label>Message outputs</Form.Label>

              <Form.Control
                as="textarea"
                rows={3}
                value={messages.map((message) => message + "\n")}
              ></Form.Control>
            </Form.Group>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};
